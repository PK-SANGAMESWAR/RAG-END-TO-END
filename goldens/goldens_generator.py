import glob, json, random
from dotenv import load_dotenv
from deepeval.synthesizer import Synthesizer
from langchain_text_splitters.character import RecursiveCharacterTextSplitter

from src.retriever import CHUNK_OVERLAP, CHUNK_SIZE

load_dotenv()

OUT_PATH = "goldens/retriever_deepeval_goldens.json"
SEED = 42            # fixed so a re-run samples the same chunks


# --- reuse your own VTT cleaning + chunking (same as the retriever) ---
def load_chunks():
    texts = []
    for path in glob.glob("data/*.vtt"):
        with open(path, encoding="utf-8") as f:
            lines = [ln.strip() for ln in f
                     if ln.strip() and ln.strip() != "WEBVTT" and "-->" not in ln]
        texts.append(" ".join(lines))
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    return splitter.split_text("\n\n".join(texts))


# --- generate ---
chunks = load_chunks()
random.seed(SEED)
sample = random.sample(chunks, min(15, len(chunks)))      # keep the set small
contexts = [[c] for c in sample]                          # each context = one chunk

synthesizer = Synthesizer(model="gpt-4.1-mini")                # the generator/critic model -- pin it
goldens = synthesizer.generate_goldens_from_contexts(
    contexts=contexts,
    include_expected_output=True,       # <-- THIS gives you the ideal_answer
    max_goldens_per_context=1,          # 1 question per chunk -> ~12 goldens
)


# --- convert to YOUR schema (id / query / ideal_answer / source) ---
rows = []
for i, g in enumerate(goldens, 1):
    rows.append({
        "id": f"g{i:03d}",
        "query": g.input,
        "ideal_answer": g.expected_output,
        "source": "TODO-verify",        # Synthesizer won't know the session -- you fill this
    })

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2, ensure_ascii=False)

print(f"wrote {len(rows)} DRAFT goldens -> {OUT_PATH}")
print("!! REVIEW EVERY ONE before using: check grounding, trim padding, fix leading questions.")