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
(RAG-END-TO-END) PS C:\Users\LOQ\Downloads\RAG-END-TO-END> G-END-TO-END) PS C:\Users\LOQ\Downloads\RAG-END-TO-END> 
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████| 105/105 [00:00<00:00, 6183.94it/s]
✨ You're running DeepEval's latest Contextual Relevancy Metric! 
(using gpt-4o-mini, strict=False, async_mode=True)...
✨ You're running DeepEval's latest Faithfulness Metric! (using 
gpt-4o-mini, strict=False, async_mode=True)...
✨ You're running DeepEval's latest Answer Relevancy Metric! (using 
gpt-4o-mini, strict=False, async_mode=True)...

╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ 🚀 DeepEval Evaluation Results                                                                                                                                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_0                                                                                                                                                             │
│  ├──   Input:            what is vibe testing and why isn't it enough for deploying an llm app?                                                                             │
│  │     Actual Output:    Vibe testing is a casual and informal way of evaluating a large language model (LLM) application. Essentially, it involves trying out the          │
│  │                       application by asking a few prompts—typically around five to ten questions—and then judging the responses based on your personal feelings or       │
│  │                       impressions. If the answers seem right to you, you might conclude that the application is functioning well. However, this method is subjective     │
│  │                       and not repeatable; the questions you ask today may differ from those you ask in the future, which means the evaluation can vary significantly     │
│  │                       over time.                                                                                                                                         │
│  │                                                                                                                                                                          │
│  │                       Now, regarding why vibe testing isn't sufficient for deploying an LLM application, there are several important points to consider. First, vibe     │
│  │                       testing is primarily suited for personal projects and lacks the rigor needed for production-grade software. In a professional setting,             │
│  │                       deploying an application without thorough testing can lead to significant issues, especially when users interact with the software in              │
│  │                       unpredictable ways.                                                                                                                                │
│  │                                                                                                                                                                          │
│  │                       Moreover, the context emphasizes that proper evaluation is crucial before deployment. It mentions that teams have made mistakes by relying         │
│  │                       solely on vibe testing, leading to problematic deployments, as seen in case studies like Air Canada and Chart GPT. The evaluation process          │
│  │                       should be systematic and methodical, which is not the case with vibe testing.                                                                      │
│  │                                                                                                                                                                          │
│  │                       In contrast, more formal evaluation methods, such as offline evaluations, allow for pre-release testing and can be automated. This means that      │
│  │                       you can set specific criteria—like achieving a certain performance threshold—before deploying the software. This structured approach helps         │
│  │                       ensure that the application is robust and reliable, reducing the risk of issues once it is in use.                                                 │
│  │                                                                                                                                                                          │
│  │                       In summary, while vibe testing can provide a quick and informal sense of an LLM application's performance, it lacks the thoroughness and           │
│  │                       repeatability necessary for safe deployment in a production environment.                                                                           │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.56  │ 0.70      │ The score is 0.56 because while there are relevant statements about vibe testing, such as 'Vibe testing means     │
│              │                      │       │           │ you casually trying an LLME application with a few prompts and judging it by feel.' and 'By doing vibe testing,   │
│              │                      │       │           │ you don't make production grade software in the industry.', many other statements in the context do not address   │
│              │                      │       │           │ the input question, leading to a lower relevancy score.                                                           │
│        PASS  │ Faithfulness         │ 0.93  │ 0.70      │ The score is 0.93 because the actual output inc...                                                                │
│        PASS  │ Answer Relevancy     │ 1.00  │ 0.70      │ The score is 1.00 because the response directly...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_1                                                                                                                                                             │
│  ├──   Input:            what is the mmlu benchmark?                                                                                                                        │
│  │     Actual Output:    The MMLU benchmark, which stands for "Massive Multitask Language Understanding," is a significant evaluation tool used to assess the knowledge     │
│  │                       capabilities of large language models (LLMs). Launched in September 2020, MMLU consists of a dataset that includes around 14,000                   │
│  │                       multiple-choice questions covering 57 different subjects. These subjects range widely, encompassing areas such as science, history, law, and       │
│  │                       medicine.                                                                                                                                          │
│  │                                                                                                                                                                          │
│  │                       The primary purpose of MMLU is to measure the breadth of knowledge that an LLM possesses. This means it evaluates how much general knowledge       │
│  │                       the model has rather than how deeply it understands specific topics. The questions in the MMLU dataset are sourced from real exams, such as the    │
│  │                       USMLE (United States Medical Licensing Examination) and the USGRE (United States Graduate Record Examinations), as well as other educational       │
│  │                       materials, which may include textbooks and online resources.                                                                                       │
│  │                                                                                                                                                                          │
│  │                       When researchers or developers want to test an LLM, they present it with these 14,000 questions and record how many the model answers              │
│  │                       correctly. The accuracy score derived from this testing provides insights into the model's knowledge level. However, it's important to note        │
│  │                       that over time, as these questions become publicly available, they can inadvertently become part of the training data for newer models. This       │
│  │                       leads to a phenomenon known as "contamination," where subsequent models may perform better simply because they have seen the questions before,     │
│  │                       rather than because they possess a deeper understanding.                                                                                           │
│  │                                                                                                                                                                          │
│  │                       In summary, MMLU serves as a foundational benchmark in the field of LLM evaluations, helping to quantify how knowledgeable a model is across a     │
│  │                       wide array of subjects.                                                                                                                            │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.48  │ 0.70      │ The score is 0.48 because while there are relevant statements about the MMLU benchmark, such as 'MMLU is          │
│              │                      │       │           │ basically a data set in which around 57 subjects there are 14,000 questions MCQ' and 'this benchmark tests how    │
│              │                      │       │           │ much breadth of knowledge it has not depth of knowledge,' the majority of the retrieval context focuses on        │
│              │                      │       │           │ unrelated topics like contamination in LLM training data and general benchmark discussions, which detracts from   │
│              │                      │       │           │ the overall relevance.                                                                                            │
│        PASS  │ Faithfulness         │ 0.92  │ 0.70      │ The score is 0.92 because the actual output inc...                                                                │
│        PASS  │ Answer Relevancy     │ 1.00  │ 0.70      │ The score is 1.00 because the response directly...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_2                                                                                                                                                             │
│  ├──   Input:            how did mmlu pro improve on the original mmlu?                                                                                                     │
│  │     Actual Output:    MMLU Pro improved on the original MMLU by addressing several key issues that were identified in the earlier benchmark. The original MMLU was       │
│  │                       considered saturated, meaning that it became difficult to distinguish between the performance of different models because many were achieving      │
│  │                       similar high scores. This saturation was partly due to the fact that the questions in MMLU were very challenging, often at a research level,       │
│  │                       which made it hard for even advanced models to score well initially.                                                                               │
│  │                                                                                                                                                                          │
│  │                       One of the main improvements in MMLU Pro was the adjustment in the question format. While MMLU featured multiple-choice questions (MCQs) with      │
│  │                       four options, MMLU Pro expanded this to ten options per question. This change increased the difficulty level, as models now had to select the      │
│  │                       correct answer from a larger pool of choices, making it a more rigorous test of their knowledge.                                                   │
│  │                                                                                                                                                                          │
│  │                       Additionally, MMLU Pro aimed to rectify some of the flaws found in the original MMLU. For instance, it was discovered that about 6.5% of the       │
│  │                       questions in MMLU had issues, such as incorrect answers or missing correct options. By addressing these problems, MMLU Pro sought to provide a     │
│  │                       more reliable and valid assessment of a model's knowledge.                                                                                         │
│  │                                                                                                                                                                          │
│  │                       Overall, MMLU Pro was designed to be a more robust benchmark that not only maintained the strengths of MMLU but also improved upon its             │
│  │                       weaknesses, ensuring that it could effectively evaluate the capabilities of next-generation language models.                                       │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.33  │ 0.70      │ The score is 0.33 because while there are some relevant statements like 'MMLU PRO is an upgrade directly on the   │
│              │                      │       │           │ very famous MMLU benchmark' and 'MMLU Pro is a new benchmark that was created to solve the problems of MMLU',     │
│              │                      │       │           │ the majority of the context fails to directly address how MMLU Pro improves on the original MMLU, as              │
│              │                      │       │           │ highlighted by reasons such as 'The statement discusses the saturation of MMLU but does not directly address      │
│              │                      │       │           │ how MMLU PRO improves on it.'                                                                                     │
│        PASS  │ Faithfulness         │ 0.88  │ 0.70      │ The score is 0.88 because the actual output inc...                                                                │
│        FAIL  │ Answer Relevancy     │ 0.62  │ 0.70      │ The score is 0.62 because several statements in the output did not directly address the improvements made by      │
│              │                      │       │           │ MMLU Pro over the original MMLU, focusing instead on unrelated aspects such as model performance and initial      │
│              │                      │       │           │ challenges.                                                                                                       │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_3                                                                                                                                                             │
│  ├──   Input:            can you give a real-world example of an llm application failing badly?                                                                             │
│  │     Actual Output:    I don't have enough information in the course material to answer that.                                                                             │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.08  │ 0.70      │ The score is 0.08 because while the retrieval context mentions that 'Any component of any LLM application can     │
│              │                      │       │           │ fail,' it fails to provide a specific real-world example of an LLM application failing badly, which is the core   │
│              │                      │       │           │ of the input request.                                                                                             │
│        PASS  │ Faithfulness         │ 1.00  │ 0.70      │ The score is 1.00 because there are no contradi...                                                                │
│        FAIL  │ Answer Relevancy     │ 0.00  │ 0.70      │ The score is 0.00 because the response fails to provide any relevant examples of LLM applications failing,        │
│              │                      │       │           │ indicating a lack of information on the topic.                                                                    │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_4                                                                                                                                                             │
│  ├──   Input:            what is drift and why does it matter after deployment?                                                                                             │
│  │     Actual Output:    Drift refers to the gradual change in the performance or relevance of a system, particularly after it has been deployed. This concept is           │
│  │                       crucial because, over time, the conditions under which the system was initially evaluated may no longer apply. For instance, if you have a         │
│  │                       chart bot that was trained and tested with specific documents and data, as the business evolves—like changes in pricing, curriculum, or            │
│  │                       policies—the original data may become outdated. This means that the evaluations and metrics that were once accurate might no longer reflect the    │
│  │                       system's current performance.                                                                                                                      │
│  │                                                                                                                                                                          │
│  │                       Drift matters after deployment for several reasons. First, it can lead to systematic failures, such as biases or inaccuracies in the system's      │
│  │                       responses. If the system was performing well initially but starts to show a decline in metrics like faithfulness or accuracy, it indicates that    │
│  │                       drift is occurring. This decline can happen without any prior indication, making it essential to monitor the system continuously.                  │
│  │                                                                                                                                                                          │
│  │                       Moreover, recognizing drift allows for timely interventions. When you detect that a certain metric is dropping, you can alert the team and take    │
│  │                       steps to improve the system. This might involve updating the training data or refining the model based on new information. Essentially, drift      │
│  │                       highlights the need for ongoing evaluation and adaptation of the system to ensure it remains effective and relevant in a changing environment.     │
│  │                                                                                                                                                                          │
│  │                       In summary, drift is a natural occurrence in deployed systems, and understanding it is vital for maintaining the system's performance and          │
│  │                       reliability over time.                                                                                                                             │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.50  │ 0.70      │ The score is 0.50 because while there are relevant statements about drift, such as 'drift can occur in the        │
│              │                      │       │           │ picture' and 'Drift means that basically, Your offline eval... starts to get obsolete,' many other statements     │
│              │                      │       │           │ are irrelevant, discussing topics like 'emergent systematic failures' and 'user behavior,' which do not address   │
│              │                      │       │           │ the importance of drift after deployment.                                                                         │
│        PASS  │ Faithfulness         │ 1.00  │ 0.70      │ The score is 1.00 because there are no contradi...                                                                │
│        PASS  │ Answer Relevancy     │ 1.00  │ 0.70      │ The score is 1.00 because the response directly...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_5                                                                                                                                                             │
│  ├──   Input:            why do we use an llm as a judge instead of simple string matching?                                                                                 │
│  │     Actual Output:    Using an LLM as a judge instead of simple string matching is primarily about the depth and flexibility of understanding that LLMs provide.         │
│  │                       String matching is a straightforward technique that looks for exact matches between the input and a predefined set of answers. While this can      │
│  │                       be effective for very specific or straightforward questions, it falls short in many scenarios, especially when dealing with open-ended             │
│  │                       questions or nuanced responses.                                                                                                                    │
│  │                                                                                                                                                                          │
│  │                       LLMs, on the other hand, are designed to understand context, semantics, and the subtleties of language. They can evaluate answers based on         │
│  │                       meaning rather than just matching words. For instance, if a question has a complex answer that requires interpretation or elaboration, an LLM      │
│  │                       can assess the quality and relevance of the response more effectively than simple string matching could. This is particularly important in         │
│  │                       educational settings or assessments where the answers may vary widely in phrasing but still convey the same underlying concept.                    │
│  │                                                                                                                                                                          │
│  │                       Moreover, as the context mentions, LLMs have improved over time, leading to better accuracy in extracting correct answers. This means that they    │
│  │                       can adapt to different types of questions and provide a more reliable evaluation compared to static string matching methods. In essence, using     │
│  │                       an LLM as a judge allows for a more sophisticated and accurate assessment of answers, especially in cases where the evaluation criteria are not    │
│  │                       strictly defined or where answers can be expressed in multiple valid ways.                                                                         │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.48  │ 0.70      │ The score is 0.48 because while there are relevant statements like 'we use LLM as a judge to evaluate open        │
│              │                      │       │           │ ended answers' and 'the capability of the LLM as a judge has increased in the last two years', many other         │
│              │                      │       │           │ statements do not address the core question, such as 'there is a problem here' and 'the point of scoring and      │
│              │                      │       │           │ the last is aggregation', which detract from the overall relevance.                                               │
│        PASS  │ Faithfulness         │ 1.00  │ 0.70      │ The score is 1.00 because there are no contradi...                                                                │
│        PASS  │ Answer Relevancy     │ 1.00  │ 0.70      │ The score is 1.00 because the response directly...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_6                                                                                                                                                             │
│  ├──   Input:            how does sampling work in online evaluation?                                                                                                       │
│  │     Actual Output:    Sampling in online evaluation is a technique used to manage the costs and complexity of monitoring a large number of conversations. In the         │
│  │                       context provided, when a chatbot interacts with 50,000 users in a day, it would be impractical and expensive to evaluate every single              │
│  │                       conversation. Instead, sampling allows evaluators to randomly select a smaller subset of those conversations for analysis.                         │
│  │                                                                                                                                                                          │
│  │                       Specifically, the process involves randomly selecting 1,000 conversations from the total of 50,000. This smaller group is then evaluated using     │
│  │                       a language model (LLM) that acts as a judge to assess the quality of the interactions. The evaluator provides a metric known as the                │
│  │                       hallucination rate, which indicates how often the model generates incorrect or nonsensical responses. This metric is then aggregated over time     │
│  │                       and displayed on a dashboard, allowing for ongoing monitoring of the chatbot's performance.                                                        │
│  │                                                                                                                                                                          │
│  │                       Additionally, the context mentions the use of stratified sampling, which is a more refined approach. This means that instead of just random        │
│  │                       sampling, the selection process takes into account different categories of conversations. For instance, if certain types of conversations are      │
│  │                       more likely to exhibit issues, more samples from those categories would be included in the evaluation. This targeted approach increases the        │
│  │                       likelihood of detecting problems, such as hallucinations, in the chatbot's responses.                                                              │
│  │                                                                                                                                                                          │
│  │                       In summary, sampling in online evaluation is about efficiently selecting a manageable number of conversations for analysis, ensuring that the      │
│  │                       evaluation remains cost-effective while still providing valuable insights into the chatbot's performance.                                          │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.41  │ 0.70      │ The score is 0.41 because while there are relevant statements about sampling, such as 'you randomly select 1000   │
│              │                      │       │           │ conversations randomly' and 'the sampling type technique is used', the majority of the retrieval context          │
│              │                      │       │           │ focuses on unrelated aspects like costs and alerts, which do not explain how sampling works in online             │
│              │                      │       │           │ evaluation.                                                                                                       │
│        PASS  │ Faithfulness         │ 0.90  │ 0.70      │ The score is 0.90 because the actual output inc...                                                                │
│        PASS  │ Answer Relevancy     │ 1.00  │ 0.70      │ The score is 1.00 because the response directly...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_7                                                                                                                                                             │
│  ├──   Input:            what are computed and captured signals in online eval?                                                                                             │
│  │     Actual Output:    In the context of online evaluation, signals are categorized into two distinct types: computed signals and captured signals.                       │
│  │                                                                                                                                                                          │
│  │                       Computed signals are those that require calculation or analysis to derive meaningful metrics. For instance, if you want to assess the              │
│  │                       faithfulness of a chatbot's responses, you can't just look at the conversation logs; you need to send that data to an online evaluator that        │
│  │                       will compute a faithfulness score. Other examples of computed signals include answer relevance, correctness, hallucination, toxicity, bias, and    │
│  │                       fairness. These metrics are not directly observable and must be calculated based on the interactions and responses generated by the chatbot.       │
│  │                                                                                                                                                                          │
│  │                       On the other hand, captured signals are those that are readily available and do not require any calculation. These are signals that you simply     │
│  │                       store as they are. For example, if a user gives a thumbs up or thumbs down during a conversation, that feedback is a captured signal.              │
│  │                       Similarly, latency, which measures how long it takes for the chatbot to respond, is also a captured signal. You can directly store this            │
│  │                       information without needing to compute anything. Other examples include cost per conversation and token usage, which are also stored as they       │
│  │                       are provided by the LLM provider.                                                                                                                  │
│  │                                                                                                                                                                          │
│  │                       In summary, computed signals involve analysis and calculation to derive insights, while captured signals are straightforward data points that      │
│  │                       are stored directly without further processing.                                                                                                    │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.56  │ 0.70      │ The score is 0.56 because while there are relevant statements like 'there are actually two types of signals       │
│              │                      │       │           │ which you have to focus on' and 'computed signals are those that you have to calculate or figure out', the        │
│              │                      │       │           │ majority of the context contains irrelevant information such as 'Everything is very simple and straightforward'   │
│              │                      │       │           │ and 'This is all chatbot related', which do not address the specifics of computed and captured signals.           │
│        PASS  │ Faithfulness         │ 1.00  │ 0.70      │ The score is 1.00 because there are no contradi...                                                                │
│        PASS  │ Answer Relevancy     │ 0.91  │ 0.70      │ The score is 0.91 because while the response pr...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_8                                                                                                                                                             │
│  ├──   Input:            what does it mean for a benchmark to get saturated?                                                                                                │
│  │     Actual Output:    Benchmark saturation occurs when a particular benchmark, which is a standard used to evaluate the performance of models, becomes less effective    │
│  │                       at distinguishing between different models because they all achieve similar high scores. Initially, when a benchmark is introduced, models may     │
│  │                       perform poorly on it, as they are not yet familiar with the specific questions or tasks it presents. Over time, as models improve and adapt,       │
│  │                       their scores on this benchmark increase significantly.                                                                                             │
│  │                                                                                                                                                                          │
│  │                       For example, when a benchmark is first released, models might score around 25% or 36%. However, as the models are trained and refined, their       │
│  │                       performance can rise to 90% or even higher. Eventually, many models cluster around the same high score, such as 94% to 95%, making it difficult    │
│  │                       to differentiate which model is truly better. This clustering indicates that the benchmark has become saturated; it no longer provides             │
│  │                       meaningful insights into the relative performance of the models.                                                                                   │
│  │                                                                                                                                                                          │
│  │                       When saturation occurs, the benchmark is often retired and replaced with a new one to ensure that there is still a way to evaluate and compare     │
│  │                       the capabilities of different models effectively. In essence, benchmark saturation highlights the lifecycle of benchmarks in the field of model    │
│  │                       evaluation, where they become less useful as models improve and achieve similar results.                                                           │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.35  │ 0.70      │ The score is 0.35 because while there are relevant statements explaining benchmark saturation, such as 'this      │
│              │                      │       │           │ means that this benchmark is no longer useful you can't differentiate the models' and 'everyone starts scoring    │
│              │                      │       │           │ well then your benchmark is saturated', the majority of the retrieval context focuses on unrelated topics like    │
│              │                      │       │           │ model alignment and configuration gaming, which detracts from the overall relevance.                              │
│        PASS  │ Faithfulness         │ 0.89  │ 0.70      │ The score is 0.89 because the actual output inc...                                                                │
│        PASS  │ Answer Relevancy     │ 1.00  │ 0.70      │ The score is 1.00 because the response directly...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_9                                                                                                                                                             │
│  ├──   Input:            how are safety issues like toxicity evaluated differently from quality issues?                                                                     │
│  │     Actual Output:    Great question! To understand how safety issues like toxicity are evaluated differently from quality issues, we first need to clarify what each    │
│  │                       of these terms means in the context of evaluating language models.                                                                                 │
│  │                                                                                                                                                                          │
│  │                       When we talk about **safety issues**, we're primarily concerned with ensuring that the responses generated by the model do not cause harm. This    │
│  │                       includes checking for toxicity, which refers to harmful or offensive content, as well as other safety-related aspects like the presence of         │
│  │                       dangerous content, biased responses, and the potential for leaking personally identifiable information (PII). The evaluation process for safety    │
│  │                       involves specific metrics that focus on these harmful elements, ensuring that the model's outputs are safe for users.                              │
│  │                                                                                                                                                                          │
│  │                       On the other hand, **quality issues** relate to how well the model performs its intended function. This includes evaluating whether the answers    │
│  │                       provided are correct, relevant, and complete. For instance, if a user asks a question with multiple parts, a quality evaluation would check if     │
│  │                       the model addresses all parts of the question adequately. Completeness is a key metric here, as it assesses whether the response fully answers     │
│  │                       the user's inquiry. Additionally, quality evaluations may also consider the style of the response, ensuring it aligns with expected standards.     │
│  │                                                                                                                                                                          │
│  │                       In summary, while safety evaluations focus on preventing harm and ensuring the model does not produce toxic or dangerous content, quality          │
│  │                       evaluations are about the effectiveness and accuracy of the model's responses. Each type of evaluation has its own set of criteria and metrics     │
│  │                       tailored to its specific goals, which is crucial for a comprehensive assessment of the model's performance.                                        │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.24  │ 0.70      │ The score is 0.24 because while there are some relevant statements like 'In safety it is different for            │
│              │                      │       │           │ toxicity' and 'you see that the answer should not be toxic', the majority of the context discusses unrelated      │
│              │                      │       │           │ topics such as 'quality hallucination' and 'image-based chat bots', which do not address the evaluation of        │
│              │                      │       │           │ safety issues like toxicity.                                                                                      │
│        PASS  │ Faithfulness         │ 1.00  │ 0.70      │ The score is 1.00 because there are no contradi...                                                                │
│        PASS  │ Answer Relevancy     │ 0.80  │ 0.70      │ The score is 0.80 because while the response ad...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_10                                                                                                                                                            │
│  ├──   Input:            does training on more data always make an llm more knowledgeable?                                                                                  │
│  │     Actual Output:    Training on more data does not always make a large language model (LLM) more knowledgeable. While it might seem intuitive that more data would     │
│  │                       lead to a better understanding of the world, the reality is more complex. The context explains that simply increasing the amount of training       │
│  │                       data can lead to issues like the model propagating incorrect information or misconceptions found in that data.                                     │
│  │                                                                                                                                                                          │
│  │                       For instance, when LLMs like GPT-2 and GPT-3 were trained on vast amounts of internet data, they were able to answer a wide range of questions.    │
│  │                       However, this does not guarantee that they retained accurate knowledge or that their answers were reliable. The context highlights the             │
│  │                       importance of systematic evaluation processes, such as the MMLU benchmark, which was designed to assess how much world knowledge an LLM            │
│  │                       actually possesses.                                                                                                                                │
│  │                                                                                                                                                                          │
│  │                       Moreover, as models are trained on publicly available questions, they can become contaminated with this data, leading to saturation where newer    │
│  │                       models do not significantly outperform older ones. This saturation means that even if a model is trained on more data, it may not necessarily      │
│  │                       improve its knowledge or reliability.                                                                                                              │
│  │                                                                                                                                                                          │
│  │                       In summary, while training on more data can enhance an LLM's capabilities, it does not automatically translate to increased knowledge,             │
│  │                       especially if that data includes inaccuracies or misconceptions.                                                                                   │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.33  │ 0.70      │ The score is 0.33 because while there are relevant statements like 'training a big model on more data does not    │
│              │                      │       │           │ necessarily mean that you have a more knowledgeable LLM', the majority of the context fails to directly address   │
│              │                      │       │           │ the input question, as seen in statements discussing benchmarks and contamination that do not clarify the         │
│              │                      │       │           │ relationship between training data and LLM knowledge.                                                             │
│        PASS  │ Faithfulness         │ 0.88  │ 0.70      │ The score is 0.88 because the actual output sug...                                                                │
│        FAIL  │ Answer Relevancy     │ 0.60  │ 0.70      │ The score is 0.60 because the output included several statements that contradicted the premise that training on   │
│              │                      │       │           │ more data always enhances an LLM's knowledge. These irrelevant statements suggested that more data could lead     │
│              │                      │       │           │ to misunderstandings or inaccuracies, which detracted from a clear and supportive answer to the question.         │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_11 (Passed 3 metrics)                                                                                                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_12                                                                                                                                                            │
│  ├──   Input:            how can thumbs up and thumbs down signals help build a golden dataset?                                                                             │
│  │     Actual Output:    Thumbs up and thumbs down signals can play a significant role in building a golden dataset by providing direct feedback on the performance of a    │
│  │                       chatbot. When users interact with the chatbot, their responses—like giving a thumbs up or thumbs down—serve as captured signals that indicate      │
│  │                       their satisfaction or dissatisfaction with the answers provided.                                                                                   │
│  │                                                                                                                                                                          │
│  │                       To understand how this works, let's break it down. A thumbs up generally suggests that the user is happy with the response, indicating that the    │
│  │                       chatbot's answer was likely correct or satisfactory. Conversely, a thumbs down signals that the user was not satisfied, which could imply that     │
│  │                       the chatbot's response was incorrect or unhelpful. By focusing on the conversations where users gave thumbs down, evaluators can identify          │
│  │                       specific instances where the chatbot may have failed to provide accurate or relevant information.                                                  │
│  │                                                                                                                                                                          │
│  │                       This feedback is crucial for creating a golden dataset because it helps prioritize which conversations to analyze more closely. Instead of         │
│  │                       randomly sampling conversations, evaluators can concentrate on those that received thumbs down ratings. This targeted approach allows for a        │
│  │                       more efficient evaluation process, as it focuses on the areas where the chatbot needs improvement. By analyzing these negative feedback            │
│  │                       instances, evaluators can refine the chatbot's responses, ultimately contributing to the development of a more accurate and effective golden       │
│  │                       dataset.                                                                                                                                           │
│  │                                                                                                                                                                          │
│  │                       In summary, thumbs up and thumbs down signals help in building a golden dataset by providing clear indicators of user satisfaction, allowing       │
│  │                       evaluators to focus on problematic interactions and improve the overall performance of the chatbot.                                                │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.39  │ 0.70      │ The score is 0.39 because while there are relevant statements like 'captured signal is thumbs up, thumbs down'    │
│              │                      │       │           │ and 'user's feedback has been done', the majority of the context discusses unrelated topics such as 'computed     │
│              │                      │       │           │ signals' and 'latency', which detracts from the overall relevance to the input question about building a golden   │
│              │                      │       │           │ dataset.                                                                                                          │
│        PASS  │ Faithfulness         │ 1.00  │ 0.70      │ The score is 1.00 because there are no contradi...                                                                │
│        PASS  │ Answer Relevancy     │ 1.00  │ 0.70      │ The score is 1.00 because the response directly...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_13                                                                                                                                                            │
│  ├──   Input:            how does a step-by-step prompt help an llm solve a math problem?                                                                                   │
│  │     Actual Output:    A step-by-step prompt helps a language model (LLM) solve a math problem by guiding it through the problem-solving process in a structured          │
│  │                       manner. When you present a math problem in a step-by-step format, it allows the LLM to break down the problem into smaller, more manageable        │
│  │                       parts. This is important because math problems often require a sequence of logical steps to arrive at the correct answer.                          │
│  │                                                                                                                                                                          │
│  │                       For instance, if you take a problem like "Natalia sold 48 divided by 2," a step-by-step prompt would lead the LLM to first recognize that it       │
│  │                       needs to perform the division, which results in 24. Then, it can proceed to the next part of the problem, such as adding that result to another    │
│  │                       number, like in "Natalia sold 48 plus 24 clips all together." By following these steps, the LLM can systematically work through the problem        │
│  │                       rather than trying to jump to the final answer all at once.                                                                                        │
│  │                                                                                                                                                                          │
│  │                       This method is particularly effective because it reduces the chances of mistakes. If the LLM is instructed to provide a direct answer without      │
│  │                       the chain of thought, it may overlook critical steps or misinterpret the problem. By allowing a step-by-step approach, the LLM can clarify its     │
│  │                       reasoning and ensure that each part of the problem is addressed correctly.                                                                         │
│  │                                                                                                                                                                          │
│  │                       In summary, a step-by-step prompt enhances the LLM's ability to solve math problems by providing a clear framework for reasoning, which helps      │
│  │                       it to arrive at accurate answers through logical progression.                                                                                      │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.50  │ 0.70      │ The score is 0.50 because while some statements like 'kind of system prompt that see this question and try to     │
│              │                      │       │           │ solve it step by step' are relevant, many others focus on unrelated topics such as instruction following and      │
│              │                      │       │           │ benchmarks, which do not directly address how a step-by-step prompt aids in solving math problems.                │
│        PASS  │ Faithfulness         │ 0.89  │ 0.70      │ The score is 0.89 because the actual output inc...                                                                │
│        PASS  │ Answer Relevancy     │ 0.93  │ 0.70      │ The score is 0.93 because while the response ef...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                             │
│  ❌ test_case_14                                                                                                                                                            │
│  ├──   Input:            what are computed and captured signals in online evaluation?                                                                                       │
│  │     Actual Output:    In online evaluation, we focus on two distinct types of signals: computed signals and captured signals.                                            │
│  │                                                                                                                                                                          │
│  │                       Let's start with captured signals. These are signals that are already present and simply need to be stored without any additional calculation.     │
│  │                       For example, if a user gives a thumbs up or thumbs down during a conversation, that feedback is a captured signal. You take that input directly    │
│  │                       and store it in a system like Langsmith. Another example of a captured signal is latency, which measures how long it takes for the chatbot to      │
│  │                       respond. This is also stored as is, without any need for calculation. Similarly, cost per conversation, which refers to how many tokens or how     │
│  │                       much money was spent, is another captured signal. You don't need to compute these values in real-time; they are recorded as they are.              │
│  │                                                                                                                                                                          │
│  │                       Now, moving on to computed signals, these require some level of calculation or evaluation. For instance, if you want to assess the faithfulness    │
│  │                       of your chatbot's responses, you can't just store the conversation; you need to send it to an online evaluator that will compute a faithfulness    │
│  │                       score. Other examples of computed signals include answer relevance, correctness, hallucination, toxicity, bias, and fairness. These metrics are    │
│  │                       not simply captured; they require analysis to determine how well the chatbot is performing in these areas.                                         │
│  │                                                                                                                                                                          │
│  │                       In summary, captured signals are straightforward inputs that you store directly, while computed signals involve calculations that provide          │
│  │                       deeper insights into the chatbot's performance. Understanding the difference between these two types of signals is crucial for effective online    │
│  │                       evaluation.                                                                                                                                        │
│  └── Metrics                                                                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        FAIL  │ Contextual Relevancy │ 0.56  │ 0.70      │ The score is 0.56 because while there are relevant statements like 'The first one is computed and the second      │
│              │                      │       │           │ one is captured signals.' and 'Computed signals are those that you have to calculate or figure out.', many        │
│              │                      │       │           │ other statements provide irrelevant information about PII, logging processes, and general chatbot discussions     │
│              │                      │       │           │ that do not address the input question.                                                                           │
│        PASS  │ Faithfulness         │ 1.00  │ 0.70      │ The score is 1.00 because there are no contradi...                                                                │
│        PASS  │ Answer Relevancy     │ 1.00  │ 0.70      │ The score is 1.00 because the response directly...                                                                │
│                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Aggregate Metrics                                                                                                                                                           │
│                                                                                                                                                                             │
│  Metric                                          ┃ Average Score                    ┃ Pass Rate                                                            ┃ Total          │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━ │
│  Contextual Relevancy                            │ 0.44                             │ 6.67% | passed=1 | failed=14                                         │ 15             │
│  Faithfulness                                    │ 0.95                             │ 100.00% | passed=15 | failed=0                                       │ 15             │
│  Answer Relevancy                                │ 0.86                             │ 80.00% | passed=12 | failed=3                                        │ 15             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


⚠ WARNING: No hyperparameters logged.





 You're running DeepEval's latest Correctness [GEval] Metric! (using gpt-4o-mini, 
strict=False, async_mode=True)...
✨ You're running DeepEval's latest Completeness [GEval] Metric! (using gpt-4o-mini, 
strict=False, async_mode=True)...
✨ You're running DeepEval's latest Style [GEval] Metric! (using gpt-4o-mini, strict=False, 
async_mode=True)...
Warning: Could not load test run from disk: Shared locks on Windows require the win32 extra 
(pywin32); msvcrt provides no true shared lock. Install it with: pip install "portalocker"
In get_cached_test_run, temp=False, Lock acquisition failed: Shared locks on Windows require the win32 extra (pywin32); msvcrt 
provides no true shared lock. Install it with: pip install "portalocker[win32]"
In get_cached_test_run, temp=True, Lock acquisition failed: Shared locks on Windows require the win32 extra (pywin32); msvcrt 
provides no true shared lock. Install it with: pip install "portalocker[win32]"

╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ 🚀 DeepEval Evaluation Results                                                                                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_0 (Passed 3 metrics)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                             │
│  ❌ test_case_1                                                                                                             │
│  ├──   Input:              what's the difference between model evals and application evals?                                 │
│  │     Actual Output:      The difference between model evals and application evals lies primarily in what they are         │
│  │                         designed to evaluate. Model evals focus on assessing the capabilities of the language models     │
│  │                         (LLMs) themselves. This means that when a new LLM is released, model evals are used to           │
│  │                         benchmark its performance, testing various capabilities such as reasoning, coding, or            │
│  │                         instruction following. Essentially, model evals are systematic tests that help determine how     │
│  │                         well an LLM performs on specific tasks, and the results are often documented in terms of         │
│  │                         accuracy or rankings on benchmarks.                                                              │
│  │                                                                                                                          │
│  │                         On the other hand, application evals are concerned with evaluating LLM-based applications,       │
│  │                         which are systems that incorporate LLMs as one component among many. While the LLM is a          │
│  │                         crucial part of these applications, there are other elements at play, such as the user           │
│  │                         interface, the prompts used, any additional tools or APIs integrated, and the overall            │
│  │                         orchestration of the system. Application evals assess how well the entire application            │
│  │                         functions, taking into account all these components and how they work together to deliver a      │
│  │                         seamless user experience.                                                                        │
│  │                                                                                                                          │
│  │                         In summary, model evals are about testing the LLM itself, while application evals focus on       │
│  │                         the performance of applications that utilize LLMs, considering the broader context in which      │
│  │                         the LLM operates.                                                                                │
│  │     Expected Output:    Model evals test the capabilities of the raw LLM itself, independent of any product, and         │
│  │                         include benchmarks as well as custom model evals used to pick a model. Application evals test    │
│  │                         a system built around one or more LLMs, such as a RAG chatbot or an agent, evaluated             │
│  │                         end-to-end. In short, model evals judge the model, application evals judge the system you        │
│  │                         built.                                                                                           │
│  └── Metrics                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        PASS  │ Correctness [GEval]  │ 0.86  │ 0.70      │ The response accurately distinguishes between m...                │
│        PASS  │ Completeness [GEval] │ 0.78  │ 0.70      │ The response effectively distinguishes between ...                │
│        FAIL  │ Style [GEval]        │ 0.62  │ 0.70      │ The response is understandable and provides a clear distinction   │
│              │                      │       │           │ between model evals and application evals. However, it leans      │
│              │                      │       │           │ towards a more formal tone and includes some technical jargon     │
│              │                      │       │           │ without sufficient unpacking, which detracts from a fully         │
│              │                      │       │           │ conversational style. While the explanation is coherent, it       │
│              │                      │       │           │ could benefit from a more engaging and intuitive approach to      │
│              │                      │       │           │ align better with a teaching voice.                               │
│                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                             │
│  ❌ test_case_2                                                                                                             │
│  ├──   Input:              what are the different methods to actually perform an eval?                                      │
│  │     Actual Output:      In the context of evaluating large language models (LLMs), there are three distinct methods      │
│  │                         to perform an evaluation. These methods are crucial because they determine how we assess         │
│  │                         whether an LLM's output is good or not.                                                          │
│  │                                                                                                                          │
│  │                         The first method is the **programmatic or deterministic method**. This approach relies on        │
│  │                         predefined algorithms or scripts to evaluate the output of the LLM. Essentially, it uses a       │
│  │                         set of rules or criteria to automatically judge the quality of the output without human          │
│  │                         intervention.                                                                                    │
│  │                                                                                                                          │
│  │                         The second method involves **human evaluation**. In this case, actual people assess the LLM's    │
│  │                         output. Human evaluators can provide nuanced feedback and insights that might be missed by       │
│  │                         automated systems, making this method valuable for understanding the quality of the output in    │
│  │                         a more subjective manner.                                                                        │
│  │                                                                                                                          │
│  │                         The third method is known as **model graded or LLM graded evaluation**. Here, another LLM is     │
│  │                         used to evaluate the output of the primary LLM. This method leverages the capabilities of one    │
│  │                         model to assess the performance of another, which can be particularly useful in scenarios        │
│  │                         where human evaluation is impractical or when scaling evaluations.                               │
│  │                                                                                                                          │
│  │                         These three methods—programmatic, human, and model graded—each have their strengths and can      │
│  │                         be chosen based on the specific needs of the evaluation process. Understanding these methods     │
│  │                         is essential for creating an effective evaluation pipeline for LLMs.                             │
│  │     Expected Output:    There are three broad methods. Programmatic (deterministic) evaluation uses code and fixed       │
│  │                         rules to check the output, which is cheap and reliable but only works when correctness can be    │
│  │                         expressed in code. LLM-as-a-judge uses a capable LLM to score outputs, which handles             │
│  │                         subjective or semantic judgments at scale. Human evaluation uses people to judge outputs,        │
│  │                         which is the most reliable for nuanced quality but the slowest and most expensive.               │
│  └── Metrics                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        PASS  │ Correctness [GEval]  │ 0.96  │ 0.70      │ The actual output accurately describes the thre...                │
│        PASS  │ Completeness [GEval] │ 0.82  │ 0.70      │ The response effectively covers the three key m...                │
│        FAIL  │ Style [GEval]        │ 0.63  │ 0.70      │ The response is understandable and provides a clear explanation   │
│              │                      │       │           │ of the three evaluation methods for LLMs. However, it leans       │
│              │                      │       │           │ towards a more formal tone and includes some jargon without       │
│              │                      │       │           │ sufficient unpacking, which detracts from a fully                 │
│              │                      │       │           │ conversational style. While the structure is logical, it could    │
│              │                      │       │           │ benefit from a more engaging and intuitive delivery to align      │
│              │                      │       │           │ better with a teaching voice.                                     │
│                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                             │
│  ❌ test_case_3                                                                                                             │
│  ├──   Input:              what does reference-based vs reference-free eval mean?                                           │
│  │     Actual Output:      Reference-based evaluation and reference-free evaluation are two distinct approaches to          │
│  │                         assessing the performance of models, particularly in the context of language models.             │
│  │                                                                                                                          │
│  │                         Reference-based evaluation is when you have a predefined correct answer or answer key for        │
│  │                         each test case. This means that for every output generated by the model, you can compare it      │
│  │                         against this known correct answer to determine how well the model performed. Essentially, you    │
│  │                         are grading the model's output based on how closely it matches the reference answer. An          │
│  │                         example of this type of evaluation is when you have a golden dataset that contains the           │
│  │                         correct answers, allowing you to assess the model's accuracy directly.                           │
│  │                                                                                                                          │
│  │                         On the other hand, reference-free evaluation occurs when there is no predefined correct          │
│  │                         answer available. In this case, the evaluation relies on human judgment or other methods to      │
│  │                         assess the quality of the model's output. Since there is no answer key to compare against,       │
│  │                         evaluators must use their discretion, often guided by a rubric, to determine the quality of      │
│  │                         the responses. This type of evaluation is useful in scenarios where the answers can be           │
│  │                         subjective or where multiple valid responses might exist.                                        │
│  │                                                                                                                          │
│  │                         In summary, the key difference lies in the availability of a correct answer: reference-based     │
│  │                         evaluation has a known answer for comparison, while reference-free evaluation does not,          │
│  │                         relying instead on human judgment or alternative methods to assess performance.                  │
│  │     Expected Output:    A reference-based eval needs a ground-truth answer to compare against, a golden or expected      │
│  │                         output authored ahead of time, and scores the system by how close it comes to that reference.    │
│  │                         A reference-free eval needs no ground truth and instead judges an intrinsic property of the      │
│  │                         output, usually with an LLM as a judge. The test is simply whether the metric requires an        │
│  │                         expected answer.                                                                                 │
│  └── Metrics                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        PASS  │ Correctness [GEval]  │ 0.91  │ 0.70      │ The response accurately describes both referenc...                │
│        PASS  │ Completeness [GEval] │ 0.78  │ 0.70      │ The response effectively covers the main distin...                │
│        FAIL  │ Style [GEval]        │ 0.63  │ 0.70      │ The response is understandable and provides a clear explanation   │
│              │                      │       │           │ of the concepts of reference-based and reference-free             │
│              │                      │       │           │ evaluation. However, it leans towards a more formal tone and      │
│              │                      │       │           │ includes some structured elements that detract from a             │
│              │                      │       │           │ conversational style. While it effectively explains the ideas,    │
│              │                      │       │           │ it could benefit from a more engaging and intuitive delivery,     │
│              │                      │       │           │ perhaps by incorporating a relatable analogy or example.          │
│                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_4 (Passed 3 metrics)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_5 (Passed 3 metrics)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_6 (Passed 3 metrics)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_7 (Passed 3 metrics)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_8 (Passed 3 metrics)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                             │
│  ❌ test_case_9                                                                                                             │
│  ├──   Input:              what is a benchmark and what does MMLU test?                                                     │
│  │     Actual Output:      A benchmark is essentially a standardized test designed to evaluate the performance of a         │
│  │                         system, in this case, a language model (LLM). It serves several purposes: it defines what        │
│  │                         specific task is being measured, provides a dataset with questions and answers, outlines the     │
│  │                         conditions under which the test will be executed, and specifies how the results will be          │
│  │                         scored and aggregated. All of these details are typically documented in a research paper         │
│  │                         associated with the benchmark.                                                                   │
│  │                                                                                                                          │
│  │                         Now, when we talk about MMLU, which stands for "Massive Multitask Language Understanding," it    │
│  │                         is a specific benchmark that tests the breadth of knowledge of an LLM. Launched in September     │
│  │                         2020, MMLU consists of a dataset that includes around 14,000 multiple-choice questions           │
│  │                         covering 57 different subjects. The primary goal of MMLU is to assess how much general           │
│  │                         knowledge an LLM has, rather than how deeply it understands specific topics.                     │
│  │                                                                                                                          │
│  │                         To evaluate an LLM using MMLU, the model is presented with these multiple-choice questions,      │
│  │                         and its performance is measured by how many questions it answers correctly. This accuracy        │
│  │                         score provides insight into the model's knowledge capabilities. However, it's important to       │
│  │                         note that MMLU has some limitations, such as the potential for contamination of the dataset      │
│  │                         due to its public availability, which can lead to newer models performing better simply          │
│  │                         because they have seen the questions during training.                                            │
│  │                                                                                                                          │
│  │                         In summary, a benchmark like MMLU is crucial for systematically evaluating the knowledge of      │
│  │                         LLMs, helping to understand their capabilities in a structured way.                              │
│  │     Expected Output:    A benchmark is a standardized model eval: a fixed dataset and scoring procedure used to          │
│  │                         compare the capabilities of different models on the same footing. MMLU (Massive Multitask        │
│  │                         Language Understanding) is a multiple-choice benchmark covering many subjects that measures      │
│  │                         the breadth of a model's knowledge. It does not measure reasoning depth, calibration,            │
│  │                         open-ended generation, and it is English and exam-style only.                                    │
│  └── Metrics                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        PASS  │ Correctness [GEval]  │ 0.86  │ 0.70      │ The response accurately defines a benchmark and...                │
│        PASS  │ Completeness [GEval] │ 0.72  │ 0.70      │ The response effectively defines a benchmark an...                │
│        FAIL  │ Style [GEval]        │ 0.54  │ 0.70      │ The response is understandable and provides a clear explanation   │
│              │                      │       │           │ of benchmarks and MMLU, but it leans towards a more formal tone   │
│              │                      │       │           │ and includes some jargon without sufficient unpacking. While it   │
│              │                      │       │           │ is informative, it lacks the conversational style and intuitive   │
│              │                      │       │           │ explanations that would make it feel more like a teaching         │
│              │                      │       │           │ lecture.                                                          │
│                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_10 (Passed 3 metrics)                                                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_11 (Passed 3 metrics)                                                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_12 (Passed 3 metrics)                                                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_13 (Passed 3 metrics)                                                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                             │
│  ❌ test_case_14                                                                                                            │
│  ├──   Input:              at how many levels do we evaluate a rag application and what are they?                           │
│  │     Actual Output:      In evaluating a RAG (Retrieval-Augmented Generation) application, we assess it at three          │
│  │                         distinct levels. First, we have the **component level**, where we test individual components     │
│  │                         such as the retriever and generator. This is crucial because any single component can fail,      │
│  │                         affecting the overall performance of the application.                                            │
│  │                                                                                                                          │
│  │                         Next, we move to the **pipeline level**. Here, we evaluate the entire RAG pipeline, which        │
│  │                         includes the interaction between the components. This is where we apply the RAG triad metrics    │
│  │                         to ensure that the components work together effectively.                                         │
│  │                                                                                                                          │
│  │                         Finally, we reach the **application level**. At this stage, we assess the overall application    │
│  │                         to ensure it meets specific criteria like correctness and completeness. We also check for        │
│  │                         safety and operational metrics, which are essential for user experience and reliability.         │
│  │                                                                                                                          │
│  │                         By evaluating at these three levels—component, pipeline, and application—we can ensure a         │
│  │                         comprehensive understanding of the RAG application's performance and identify any potential      │
│  │                         failure points.                                                                                  │
│  │     Expected Output:    A RAG application is evaluated at three levels. The component level tests each building block    │
│  │                         in isolation, the retriever and the generator. The pipeline level tests the retriever and        │
│  │                         generator connected together, using the RAG triad. The application level tests the full          │
│  │                         system as the user experiences it, covering quality metrics plus safety and operations.          │
│  │                         Together these levels form the eval suite you run during regression testing.                     │
│  └── Metrics                                                                                                                │
│       Status ┃ Metric               ┃ Score ┃ Threshold ┃ Reason                                                            │
│      ━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│        PASS  │ Correctness [GEval]  │ 1.00  │ 0.70      │ The actual output accurately describes the thre...                │
│        PASS  │ Completeness [GEval] │ 0.89  │ 0.70      │ The response effectively covers all three evalu...                │
│        FAIL  │ Style [GEval]        │ 0.59  │ 0.70      │ The response is understandable and provides a clear explanation   │
│              │                      │       │           │ of the three levels of evaluation for a RAG application.          │
│              │                      │       │           │ However, it leans towards a more formal tone and includes some    │
│              │                      │       │           │ jargon without unpacking it, which detracts from a fully          │
│              │                      │       │           │ conversational style. While it is informative, it could benefit   │
│              │                      │       │           │ from a more intuitive and engaging delivery.                      │
│                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Aggregate Metrics                                                                                                           │
│                                                                                                                             │
│  Metric                            ┃ Average Score          ┃ Pass Rate                                         ┃ Total     │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━ │
│  Correctness [GEval]               │ 0.91                   │ 100.00% | passed=15 | failed=0                    │ 15        │
│  Completeness [GEval]              │ 0.79                   │ 100.00% | passed=15 | failed=0                    │ 15        │
│  Style [GEval]                     │ 0.73                   │ 66.67% | passed=10 | failed=5                     │ 15        │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Warning: Could not load test run from disk: Shared locks on Windows require the win32 extra (pywin32); msvcrt provides no true 
shared lock. Install it with: pip install "portalocker"
Warning: Could not load test run from disk: Shared locks on Windows require the win32 extra (pywin32); msvcrt provides no true 
shared lock. Install it with: pip install "portalocker"

⚠ WARNING: No hyperparameters logged.
» Log hyperparameters to attribute prompts and models to your test runs.
