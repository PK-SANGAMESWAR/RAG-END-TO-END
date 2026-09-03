"""Operational reliability evaluation for the live RAG pipeline.

This is a single-user, offline smoke/regression check. It measures logical
request success separately from individual attempt success so retrying a flaky
request cannot hide the underlying instability.
"""

from __future__ import annotations

import argparse
import random
import time
from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Callable

from dotenv import load_dotenv

from src.rag_pipeline import RagPipeline

load_dotenv()


QUESTIONS = [
    "What is the difference between reference-based and reference-free evals?",
    "Explain what faithfulness measures in a RAG pipeline.",
    "How does the G-Eval metric assign a score?",
    "What is MMLU and why is contamination a problem?",
]

DEFAULT_REPEATS = 5
DEFAULT_MAX_RETRIES = 2
BACKOFF_BASE_S = 0.5
BACKOFF_CAP_S = 8.0
JITTER_FRACTION = 0.2
MIN_REQUEST_SUCCESS_RATE = 99.0
MAX_RETRIED_REQUEST_RATE = 1.0


@dataclass
class ReliabilityStats:
    """Aggregated outcomes for logical requests and their individual attempts."""

    requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    attempts: int = 0
    successful_attempts: int = 0
    failed_attempts: int = 0
    retried_requests: int = 0
    retry_attempts: int = 0
    durations_ms: list[float] = field(default_factory=list)
    failures_by_type: Counter[str] = field(default_factory=Counter)


def validate_response(response: Any) -> None:
    """Treat malformed or empty RAG responses as failures, not successes."""
    if not isinstance(response, dict):
        raise ValueError("pipeline response is not a dictionary")
    answer = response.get("answer")
    if not isinstance(answer, str) or not answer.strip():
        raise ValueError("pipeline response has no non-empty 'answer'")


def is_retryable(error: Exception) -> bool:
    """Retry only errors normally safe to retry; fail fast on bad inputs/config."""
    status_code = getattr(error, "status_code", None)
    if status_code in {408, 409, 425, 429, 500, 502, 503, 504}:
        return True

    transient_names = {
        "APIConnectionError", "APITimeoutError", "InternalServerError",
        "RateLimitError", "ServiceUnavailableError", "TimeoutError", "ConnectionError",
    }
    return error.__class__.__name__ in transient_names


def retry_delay_seconds(retry_number: int) -> float:
    """Capped exponential backoff with jitter to avoid synchronized retries."""
    base_delay = min(BACKOFF_BASE_S * (2 ** (retry_number - 1)), BACKOFF_CAP_S)
    return base_delay * random.uniform(1 - JITTER_FRACTION, 1 + JITTER_FRACTION)


def call_with_retries(
    fn: Callable[[], dict[str, Any]], stats: ReliabilityStats, max_retries: int
) -> dict[str, Any] | None:
    """Run one logical request and record every attempt accurately."""
    stats.requests += 1
    request_start = time.perf_counter()
    had_retry = False

    for attempt_index in range(max_retries + 1):
        stats.attempts += 1
        try:
            response = fn()
            validate_response(response)
            stats.successful_attempts += 1
            stats.successful_requests += 1
            stats.durations_ms.append((time.perf_counter() - request_start) * 1000)
            return response
        except Exception as error:
            stats.failed_attempts += 1
            stats.failures_by_type[type(error).__name__] += 1
            retry_allowed = attempt_index < max_retries and is_retryable(error)
            if not retry_allowed:
                stats.failed_requests += 1
                stats.durations_ms.append((time.perf_counter() - request_start) * 1000)
                print(f"FAILED: {type(error).__name__}: {error}")
                return None

            if not had_retry:
                stats.retried_requests += 1
                had_retry = True
            stats.retry_attempts += 1
            delay = retry_delay_seconds(attempt_index + 1)
            print(f"Retrying after {type(error).__name__} (attempt {attempt_index + 1}/"
                  f"{max_retries + 1}, wait {delay:.2f}s)")
            time.sleep(delay)

    raise AssertionError("unreachable")


def benchmark(pipeline: RagPipeline, repeats: int, max_retries: int) -> ReliabilityStats:
    stats = ReliabilityStats()
    total_requests = len(QUESTIONS) * repeats
    print(f"Measuring reliability: {total_requests} requests, up to {max_retries} retries each...")
    for question in QUESTIONS:
        for _ in range(repeats):
            call_with_retries(lambda: pipeline.invoke(question), stats, max_retries)
    return stats


def percent(value: int, total: int) -> float:
    return 100 * value / total if total else 0.0


def percentile(values: list[float], p: float) -> float:
    if not values:
        return float("nan")
    ordered = sorted(values)
    index = (len(ordered) - 1) * p / 100
    lower, upper = int(index), min(int(index) + 1, len(ordered) - 1)
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (index - lower)


def report(stats: ReliabilityStats) -> bool:
    request_success_rate = percent(stats.successful_requests, stats.requests)
    attempt_success_rate = percent(stats.successful_attempts, stats.attempts)
    retried_request_rate = percent(stats.retried_requests, stats.requests)

    print("\n" + "=" * 72)
    print("RELIABILITY")
    print("=" * 72)
    print(f"logical requests       : {stats.requests}")
    print(f"request success/fail   : {stats.successful_requests} / {stats.failed_requests}")
    print(f"attempt success/fail   : {stats.successful_attempts} / {stats.failed_attempts}")
    print(f"retried requests       : {stats.retried_requests} ({retried_request_rate:.2f}%)")
    print(f"retry attempts         : {stats.retry_attempts}")
    print(f"request success rate   : {request_success_rate:.2f}%")
    print(f"attempt success rate   : {attempt_success_rate:.2f}%")
    if stats.durations_ms:
        print(f"request duration p50/p95: {percentile(stats.durations_ms, 50):.0f} / "
              f"{percentile(stats.durations_ms, 95):.0f} ms (includes retry backoff)")
    if stats.failures_by_type:
        failures = ", ".join(f"{name}={count}" for name, count in stats.failures_by_type.most_common())
        print(f"failed attempts by type: {failures}")

    passed = (request_success_rate >= MIN_REQUEST_SUCCESS_RATE and
              retried_request_rate <= MAX_RETRIED_REQUEST_RATE)
    verdict = "PASS" if passed else "FAIL"
    print("-" * 72)
    print(f"GATE: request success >= {MIN_REQUEST_SUCCESS_RATE:.1f}% and retried requests <= "
          f"{MAX_RETRIED_REQUEST_RATE:.1f}%  ->  [{verdict}]")
    print("=" * 72)
    return passed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the RAG reliability evaluation.")
    parser.add_argument("--repeats", type=int, default=DEFAULT_REPEATS,
                        help=f"runs per question (default: {DEFAULT_REPEATS})")
    parser.add_argument("--max-retries", type=int, default=DEFAULT_MAX_RETRIES,
                        help=f"retries for transient failures (default: {DEFAULT_MAX_RETRIES})")
    args = parser.parse_args()
    if args.repeats < 1 or args.max_retries < 0:
        parser.error("--repeats must be >= 1 and --max-retries must be >= 0")
    return args


def main() -> None:
    args = parse_args()
    stats = benchmark(RagPipeline(), repeats=args.repeats, max_retries=args.max_retries)
    if not report(stats):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
