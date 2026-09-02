S C:\Users\LOQ\Downloads\RAG-END-TO-END> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Users\LOQ\Downloads\RAG-END-TO-END\.venv\Scripts\Activate.ps1)
(RAG-END-TO-END) PS C:\Users\LOQ\Downloads\RAG-END-TO-END> python src/retriever.py  
[Session 8] regression testing? regression testing is basically the act of running your eval suite on your application till now what we are doing we are building ...

[Session 3] choose? Then this choice will tell you your eval by running it on multiple versions of the software. This is the second benefit. Third is regression t...

[Session 8] will understand that your new version of the software is objectively better than the previous version your retriever file is telling that your new ret...

[Session 8] and what you will call this you will call this your baseline that when we run the software for the first time we got these readings after that you tho...

[Session 8] bots non LLM applications image based applications for all kinds of things you can use deep eval so that is why its adoption is also more and there is...

(RAG-END-TO-END) PS C:\Users\LOQ\Downloads\RAG-END-TO-END> 


AG-END-TO-END) PS C:\Users\LOQ\Downloads\RAG-END-TO-END> python -m evals.eval_retriever    
✨ You're running DeepEval's latest Contextual Recall Metric! (using 
gpt-4.1-mini, strict=False, async_mode=True)...
✨ You're running DeepEval's latest Contextual Precision Metric! 
(using gpt-4.1-mini, strict=False, async_mode=True)...
Warning: Could not load test run from disk: Shared locks on Windows 
require the win32 extra (pywin32); msvcrt provides no true shared 
lock. Install it with: pip install "portalocker"
In get_cached_test_run, temp=False, Lock acquisition failed: Shared locks on Windows 
require the win32 extra (pywin32); msvcrt provides no true shared lock. Install it with:
pip install "portalocker[win32]"
In get_cached_test_run, temp=True, Lock acquisition failed: Shared locks on Windows 
require the win32 extra (pywin32); msvcrt provides no true shared lock. Install it with:
pip install "portalocker[win32]"

╭──────────────────────────────────────────────────────────────────────────────────────╮
│ 🚀 DeepEval Evaluation Results                                                       │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_0 (Passed 2 metrics)                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_1 (Passed 2 metrics)                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_2 (Passed 2 metrics)                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_3 (Passed 2 metrics)                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_4 (Passed 2 metrics)                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                      │
│  ❌ test_case_5                                                                      │
│  ├──   Input:              if a model tops all the benchmarks, why wouldn't i        │
│  │                         just pick it for my project?                              │
│  │     Actual Output:      (generator not evaluated in this run)                     │
│  │     Expected Output:    The model that tops the benchmarks isn't always the       │
│  │                         best choice for your specific task. In the Zomato         │
│  │                         email-routing example, model A was a big                  │
│  │                         top-of-the-leaderboard model that beat the smaller,       │
│  │                         cheaper model B on every benchmark, so the obvious        │
│  │                         choice seemed to be model A. But when you build your      │
│  │                         own golden dataset for your actual task and run both      │
│  │                         models on it, the accuracy difference turns out to be     │
│  │                         small, while the smaller model is much cheaper and        │
│  │                         faster. So for that specific task the smaller, cheaper    │
│  │                         model is the better value, even though it is weaker       │
│  │                         overall. If you had relied only on benchmarks you         │
│  │                         would have chosen the bigger model—it is the custom       │
│  │                         eval on your own data that reveals the cheaper model      │
│  │                         is better for your work.                                  │
│  └── Metrics                                                                         │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                     │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        PASS  │ Contextual Recall    │ 1.00  │ 0.70      │ The score is 1.00          │
│              │                      │       │           │ because all sentences in   │
│              │                      │       │           │ the ...                    │
│        FAIL  │ Contextual Precision │ 0.50  │ 0.70      │ The score is 0.50          │
│              │                      │       │           │ because the first node     │
│              │                      │       │           │ in retrieval contexts,     │
│              │                      │       │           │ ranked 1st, is             │
│              │                      │       │           │ irrelevant as it           │
│              │                      │       │           │ discusses skepticism       │
│              │                      │       │           │ about benchmark numbers    │
│              │                      │       │           │ without addressing model   │
│              │                      │       │           │ choice for projects,       │
│              │                      │       │           │ while the second node,     │
│              │                      │       │           │ ranked 2nd, is relevant    │
│              │                      │       │           │ and directly explains      │
│              │                      │       │           │ why a model with top       │
│              │                      │       │           │ benchmarks might not be    │
│              │                      │       │           │ the best choice.           │
│              │                      │       │           │ However, the presence of   │
│              │                      │       │           │ multiple irrelevant        │
│              │                      │       │           │ nodes ranked above or      │
│              │                      │       │           │ near relevant ones         │
│              │                      │       │           │ limits the score from      │
│              │                      │       │           │ being higher.              │
│                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_6 (Passed 2 metrics)                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_7 (Passed 2 metrics)                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_8 (Passed 2 metrics)                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_9 (Passed 2 metrics)                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_10 (Passed 2 metrics)                                                   │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                      │
│  ❌ test_case_11                                                                     │
│  ├──   Input:              What is regression testing in LLM evaluation?             │
│  │     Actual Output:      (generator not evaluated in this run)                     │
│  │     Expected Output:    Regression testing is the act of running your full        │
│  │                         eval suite on a new version of the application to         │
│  │                         check whether it is objectively better or worse than      │
│  │                         the previous version. You run the suite, get a report     │
│  │                         of every metric, and compare it against a baseline to     │
│  │                         decide whether the new version should be deployed.        │
│  └── Metrics                                                                         │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                     │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        PASS  │ Contextual Recall    │ 1.00  │ 0.70      │ The score is 1.00          │
│              │                      │       │           │ because the expected       │
│              │                      │       │           │ output p...                │
│        FAIL  │ Contextual Precision │ 0.33  │ 0.70      │ The score is 0.33          │
│              │                      │       │           │ because the first two      │
│              │                      │       │           │ nodes in retrieval         │
│              │                      │       │           │ contexts, ranked 1st and   │
│              │                      │       │           │ 2nd, are irrelevant as     │
│              │                      │       │           │ they do not specifically   │
│              │                      │       │           │ mention regression         │
│              │                      │       │           │ testing, while the         │
│              │                      │       │           │ relevant node is ranked    │
│              │                      │       │           │ 3rd. This lowers the       │
│              │                      │       │           │ score since irrelevant     │
│              │                      │       │           │ nodes are ranked higher    │
│              │                      │       │           │ than the relevant one.     │
│              │                      │       │           │ However, the relevant      │
│              │                      │       │           │ node at rank 3 clearly     │
│              │                      │       │           │ defines regression         │
│              │                      │       │           │ testing, justifying the    │
│              │                      │       │           │ score being above zero.    │
│                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_12 (Passed 2 metrics)                                                   │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                      │
│  ❌ test_case_13                                                                     │
│  ├──   Input:              What is an eval suite?                                    │
│  │     Actual Output:      (generator not evaluated in this run)                     │
│  │     Expected Output:    An eval suite is the combined set of all the              │
│  │                         evaluation tests written across the component,            │
│  │                         pipeline, and application levels. Instead of running a    │
│  │                         single test, you run the whole suite together to check    │
│  │                         the application from every angle before deciding          │
│  │                         whether to deploy.                                        │
│  └── Metrics                                                                         │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                     │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        PASS  │ Contextual Recall    │ 1.00  │ 0.70      │ The score is 1.00          │
│              │                      │       │           │ because the expected       │
│              │                      │       │           │ output a...                │
│        FAIL  │ Contextual Precision │ 0.58  │ 0.70      │ The score is 0.58          │
│              │                      │       │           │ because the first node     │
│              │                      │       │           │ in retrieval contexts,     │
│              │                      │       │           │ ranked 1st, is             │
│              │                      │       │           │ irrelevant as it does      │
│              │                      │       │           │ not define what an eval    │
│              │                      │       │           │ suite is, while the        │
│              │                      │       │           │ relevant nodes appear at   │
│              │                      │       │           │ ranks 2 and 3, providing   │
│              │                      │       │           │ clear definitions and      │
│              │                      │       │           │ descriptions of an eval    │
│              │                      │       │           │ suite. However, the        │
│              │                      │       │           │ presence of irrelevant     │
│              │                      │       │           │ nodes ranked both above    │
│              │                      │       │           │ and below relevant         │
│              │                      │       │           │ nodes, such as the 1st     │
│              │                      │       │           │ and 4th nodes, prevents    │
│              │                      │       │           │ the score from being       │
│              │                      │       │           │ higher.                    │
│                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_14 (Passed 2 metrics)                                                   │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────╮
│ Aggregate Metrics                                                                    │
│                                                                                      │
│  Metric                 ┃ Average Score  ┃ Pass Rate                        ┃ Total  │
│ ━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━ │
│  Contextual Recall      │ 0.99           │ 100.00% | passed=15 | failed=0   │ 15     │
│  Contextual Precision   │ 0.86           │ 80.00% | passed=12 | failed=3    │ 15     │
╰──────────────────────────────────────────────────────────────────────────────────────╯

Warning: Could not load test run from disk: Shared locks on Windows require the win32 
extra (pywin32); msvcrt provides no true shared lock. Install it with: pip install 
"portalocker"
Warning: Could not load test run from disk: Shared locks on Windows require the win32 
extra (pywin32); msvcrt provides no true shared lock. Install it with: pip install 
"portalocker"

⚠ WARNING: No prompts logged.
» Log prompts to evaluate and optimize your prompt templates and models.

================================================================================


✓ Evaluation completed 🎉! (time taken: 27.18s | token cost: 0.0419308 USD)
» Test Results (15 total tests):
   » Pass Rate: 80.0% | Passed: 12 | Failed: 3

 ================================================================================ 

» Want to share evals with your team, or a place for your test cases to live? ❤️ 🏡
  » Run 'deepeval view' to analyze and save testing results on Confident AI.


[PostHog] analytics lane flush ran out of budget (1.0s granted) with 2 items pending.
(RAG-END-TO-END) PS C:\Users\LOQ\Downloads\RAG-END-TO-END> deepeval view

RAG-END-TO-END) PS C:\Users\LOQ\Downloads\RAG-END-TO-END> python -m evals.eval_retriever_with_reranker
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 105/105 [00:00<00:00, 7699.87it/s]
✨ You're running DeepEval's latest Contextual Recall Metric! (using gpt-4.1-mini, strict=False, async_mode=True)...
✨ You're running DeepEval's latest Contextual Precision Metric! (using gpt-4.1-mini, strict=False, async_mode=True)...

╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ 🚀 DeepEval Evaluation Results                                                                                                                                                │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_0 (Passed 2 metrics)                                                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_1 (Passed 2 metrics)                                                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_2 (Passed 2 metrics)                                                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_3 (Passed 2 metrics)                                                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_4 (Passed 2 metrics)                                                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                               │
│  ❌ test_case_5                                                                                                                                                               │
│  ├──   Input:              if a model tops all the benchmarks, why wouldn't i just pick it for my project?                                                                    │
│  │     Actual Output:      (generator not evaluated in this run)                                                                                                              │
│  │     Expected Output:    The model that tops the benchmarks isn't always the best choice for your specific task. In the Zomato email-routing example, model A was a big     │
│  │                         top-of-the-leaderboard model that beat the smaller, cheaper model B on every benchmark, so the obvious choice seemed to be model A. But when       │
│  │                         you build your own golden dataset for your actual task and run both models on it, the accuracy difference turns out to be small, while the         │
│  │                         smaller model is much cheaper and faster. So for that specific task the smaller, cheaper model is the better value, even though it is weaker       │
│  │                         overall. If you had relied only on benchmarks you would have chosen the bigger model—it is the custom eval on your own data that reveals the       │
│  │                         cheaper model is better for your work.                                                                                                             │
│  └── Metrics                                                                                                                                                                  │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                              │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        PASS  │ Contextual Recall    │ 1.00  │ 0.70      │ The score is 1.00 because every sentence in the...                                                                  │
│        FAIL  │ Contextual Precision │ 0.42  │ 0.70      │ The score is 0.42 because the first two nodes in the retrieval contexts, ranked 1st and 2nd, are irrelevant as      │
│              │                      │       │           │ they do not address why a top benchmark model might not be the best choice, which lowers the score. However, the    │
│              │                      │       │           │ relevant nodes ranked 3rd and 4th provide explicit examples and reasoning about choosing a smaller, more            │
│              │                      │       │           │ cost-effective model over the top benchmark model, justifying the current score.                                    │
│                                                                                                                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                               │
│  ❌ test_case_6                                                                                                                                                               │
│  ├──   Input:              what are the different ways an eval can actually be run?                                                                                           │
│  │     Actual Output:      (generator not evaluated in this run)                                                                                                              │
│  │     Expected Output:    An evaluation pipeline can be executed in one of three ways, and the distinction is simply about who is carrying out the eval. The first is        │
│  │                         programmatic, also called deterministic—a program or code executes the evaluation. The second is human—a human carries out the eval. The third     │
│  │                         is model-graded, also called LLM-graded—an LLM executes the evaluation. Any eval pipeline you build will be run by one of these three: a           │
│  │                         program, a human, or an LLM, and there's nothing beyond these three. For example, in the Zomato email-classification system, the accuracy was      │
│  │                         calculated through Python code, so that was a programmatic eval.                                                                                   │
│  └── Metrics                                                                                                                                                                  │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                              │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        PASS  │ Contextual Recall    │ 0.83  │ 0.70      │ The score is 0.83 because the retrieval context...                                                                  │
│        FAIL  │ Contextual Precision │ 0.50  │ 0.70      │ The score is 0.50 because the first node in retrieval contexts, which is irrelevant, is ranked higher than the      │
│              │                      │       │           │ relevant second node that explicitly mentions three eval methods. However, the relevant node is still ranked        │
│              │                      │       │           │ above other irrelevant nodes (third, fourth, and fifth nodes), which justifies the score being above zero but not   │
│              │                      │       │           │ higher.                                                                                                             │
│                                                                                                                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_7 (Passed 2 metrics)                                                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_8 (Passed 2 metrics)                                                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_9 (Passed 2 metrics)                                                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_10 (Passed 2 metrics)                                                                                                                                            │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_11 (Passed 2 metrics)                                                                                                                                            │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_12 (Passed 2 metrics)                                                                                                                                            │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_13 (Passed 2 metrics)                                                                                                                                            │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_14 (Passed 2 metrics)                                                                                                                                            │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Aggregate Metrics                                                                                                                                                             │
│                                                                                                                                                                               │
│  Metric                                           ┃ Average Score                    ┃ Pass Rate                                                             ┃ Total          │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━ │
│  Contextual Recall                                │ 0.99                             │ 100.00% | passed=15 | failed=0                                        │ 15             │
│  Contextual Precision                             │ 0.87                             │ 86.67% | passed=13 | failed=2                                         │ 15             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


⚠ WARNING: No prompts logged.
» Log prompts to evaluate and optimize your prompt templates and models.

================================================================================


✓ Evaluation completed 🎉! (time taken: 29.28s | token cost: 0.04308680000000001 USD)
» Test Results (15 total tests):
   » Pass Rate: 86.67% | Passed: 13 | Failed: 2

 ================================================================================ 

» Want to share evals with your team, or a place for your test cases to live? ❤️ 🏡
  » Run 'deepeval view' to analyze and save testing results on Confident AI.


[PostHog] analytics lane flush ran out of budget (1.0s granted) with 2 items pending.
(RAG-END-TO-END) PS C:\Users\LOQ\Downloads\RAG-END-TO-END> 






> G-END-TO-END) PS C:\Users\LOQ\Downloads\RAG-END-TO-END> 
✨ You're running DeepEval's latest Faithfulness Metric! (using
gpt-4o-mini, strict=False, async_mode=True)...
✨ You're running DeepEval's latest Answer Relevancy Metric! 
(using gpt-4o-mini, strict=False, async_mode=True)...
Warning: Could not load test run from disk: Shared locks on 
Windows require the win32 extra (pywin32); msvcrt provides no 
true shared lock. Install it with: pip install "portalocker"
In get_cached_test_run, temp=False, Lock acquisition failed: 
Shared locks on Windows require the win32 extra (pywin32); 
msvcrt provides no true shared lock. Install it with: pip 
install "portalocker[win32]"
In get_cached_test_run, temp=True, Lock acquisition failed: 
Shared locks on Windows require the win32 extra (pywin32); 
msvcrt provides no true shared lock. Install it with: pip 
install "portalocker[win32]"

╭─────────────────────────────────────────────────────────────╮
│ 🚀 DeepEval Evaluation Results                              │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_0 (Passed 2 metrics)                           │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_1 (Passed 2 metrics)                           │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_2 (Passed 2 metrics)                           │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│                                                             │
│  ❌ test_case_3                                             │
│  ├──   Input:            can you give a real-world          │
│  │                       example of an llm application      │
│  │                       failing badly?                     │
│  │     Actual Output:    A notable real-world example of    │
│  │                       a large language model (LLM)       │
│  │                       application failing can be seen    │
│  │                       in the case of Air Canada's        │
│  │                       chatbot. This incident occurred    │
│  │                       a couple of years ago and          │
│  │                       involved a customer who was        │
│  │                       seeking information about          │
│  │                       bereavement fares, which are       │
│  │                       discounts offered by airlines      │
│  │                       for individuals traveling due      │
│  │                       to the death of a family member    │
│  │                       or close friend.                   │
│  │                                                          │
│  │                       In this situation, the customer    │
│  │                       interacted with the chatbot on     │
│  │                       Air Canada's website.              │
│  │                       Unfortunately, the chatbot         │
│  │                       provided incorrect information,    │
│  │                       or what we refer to as             │
│  │                       "hallucinated" a response.         │
│  │                       Instead of accurately              │
│  │                       explaining the bereavement fare    │
│  │                       policy, it told the customer to    │
│  │                       book a ticket, pay the full        │
│  │                       amount upfront, and assured him    │
│  │                       that he would receive a full       │
│  │                       refund later.                      │
│  │                                                          │
│  │                       After the customer followed        │
│  │                       this advice and traveled, he       │
│  │                       attempted to get the refund as     │
│  │                       promised. However, when he         │
│  │                       contacted customer support, he     │
│  │                       was informed that such a refund    │
│  │                       policy did not exist. Air          │
│  │                       Canada had a different policy      │
│  │                       that did not allow for refunds     │
│  │                       after travel, which left the       │
│  │                       customer understandably upset.     │
│  │                                                          │
│  │                       This led to the customer filing    │
│  │                       a case against Air Canada. In      │
│  │                       court, the airline's               │
│  │                       representatives argued that the    │
│  │                       chatbot was a separate entity      │
│  │                       and that the company should not    │
│  │                       be held responsible for its        │
│  │                       statements. However, the judge     │
│  │                       ruled that since the chatbot       │
│  │                       was part of Air Canada's           │
│  │                       website, the company was indeed    │
│  │                       responsible for the information    │
│  │                       it provided. As a result, Air      │
│  │                       Canada was ordered to refund       │
│  │                       the customer approximately         │
│  │                       $600.                              │
│  │                                                          │
│  │                       This case highlights the           │
│  │                       potential risks and                │
│  │                       consequences of deploying          │
│  │                       LLM-based applications without     │
│  │                       thorough testing and oversight,    │
│  │                       particularly when they are         │
│  │                       relied upon for critical           │
│  │                       customer interactions.             │
│  └── Metrics                                                │
│       Status ┃ Metric     ┃ Score ┃ Threshold ┃ Reason      │
│      ━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━  │
│        PASS  │ Faithfuln… │ 0.71  │ 0.70      │ The score   │
│              │            │       │           │ is 0.71     │
│              │            │       │           │ because     │
│              │            │       │           │ the         │
│              │            │       │           │ actual      │
│              │            │       │           │ output      │
│              │            │       │           │ con...      │
│        FAIL  │ Answer     │ 0.67  │ 0.70      │ The score   │
│              │ Relevancy  │       │           │ is 0.67     │
│              │            │       │           │ because     │
│              │            │       │           │ while       │
│              │            │       │           │ some        │
│              │            │       │           │ relevant    │
│              │            │       │           │ points      │
│              │            │       │           │ were made   │
│              │            │       │           │ about LLM   │
│              │            │       │           │ applicat…   │
│              │            │       │           │ several     │
│              │            │       │           │ statemen…   │
│              │            │       │           │ strayed     │
│              │            │       │           │ into        │
│              │            │       │           │ backgrou…   │
│              │            │       │           │ informat…   │
│              │            │       │           │ and         │
│              │            │       │           │ unrelated   │
│              │            │       │           │ topics,     │
│              │            │       │           │ such as     │
│              │            │       │           │ airline     │
│              │            │       │           │ policies    │
│              │            │       │           │ and legal   │
│              │            │       │           │ cases,      │
│              │            │       │           │ which did   │
│              │            │       │           │ not         │
│              │            │       │           │ directly    │
│              │            │       │           │ address     │
│              │            │       │           │ the         │
│              │            │       │           │ example     │
│              │            │       │           │ of          │
│              │            │       │           │ failure     │
│              │            │       │           │ requeste…   │
│                                                             │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_4 (Passed 2 metrics)                           │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_5 (Passed 2 metrics)                           │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_6 (Passed 2 metrics)                           │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_7 (Passed 2 metrics)                           │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_8 (Passed 2 metrics)                           │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_9 (Passed 2 metrics)                           │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_10 (Passed 2 metrics)                          │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_11 (Passed 2 metrics)                          │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_12 (Passed 2 metrics)                          │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_13 (Passed 2 metrics)                          │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ ✅ test_case_14 (Passed 2 metrics)                          │
╰─────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────╮
│ Aggregate Metrics                                           │
│                                                             │
│  Metric          ┃ Average Score ┃ Pass Rate       ┃ Total  │
│ ━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━ │
│  Faithfulness    │ 0.96          │ 100.00% |       │ 15     │
│                  │               │ passed=15 |     │        │
│                  │               │ failed=0        │        │
│  Answer          │ 0.94          │ 93.33% |        │ 15     │
│  Relevancy       │               │ passed=14 |     │        │
│                  │               │ failed=1        │        │
╰─────────────────────────────────────────────────────────────╯

Warning: Could not load test run from disk: Shared locks on 
Windows require the win32 extra (pywin32); msvcrt provides no 
true shared lock. Install it with: pip install "portalocker"
Warning: Could not load test run from disk: Shared locks on 
Windows require the win32 extra (pywin32); msvcrt provides no 
true shared lock. Install it with: pip install "portalocker"

⚠ WARNING: No hyperparameters logged.
» Log hyperparameters to attribute prompts and models to your 
test runs.

===============================================================
=================


✓ Evaluation completed 🎉! (time taken: 43.43s | token cost: 
0.0189321 USD)
» Test Results (15 total tests):
   » Pass Rate: 93.33% | Passed: 14 | Failed: 1

 ==============================================================
================== 

» Want to share evals with your team, or a place for your test 
cases to live? ❤️ 🏡
  » Run 'deepeval view' to analyze and save testing results on 
Confident AI.


[PostHog] analytics lane flush ran out of budget (1.0s granted) with 2 items pending.
(RAG-END-TO-END) PS C:\Users\LOQ\Downloads\RAG-END-TO-END> 
