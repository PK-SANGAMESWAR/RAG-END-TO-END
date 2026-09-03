## Regression Testing
- Returning to a previous, less advanced or worst state.

- Eg: RAG appl -> in one point you see recall is bad -> you try to improve -> by several techniques -> system changes -> recall improved -> Due to this one aspect improvement other ascpet got regressed or got affected

- You rerun and get all results and compare with baseline results.

- If there is a significant chnge then you can use new chnge.

- Execution can be diff in diff places.

- We are using conceptual level.

- Build a script that runs the seq [Quality check -> safety check -> operational chcek]

- Run the script and save the baseline metrics

- Make chnges in the pipeline and again run the pipeline and compare with baseline metrics

- Save and compare the candidate.json

- We have baseline.json and candidate.json

- Compare the 2 json file metric by metric

- Run run_suite to get baseline and candidate and these are fed to compare.py

## Problems
- Not all metrics are same . some are good when high and some are good when low.

- Info should be given saying how metric is best ie low and high

- The eval is mostly llm as a judge except operational eval and there can be prob nature around system ie chnge in result without no chnge. 

- Need to suppress in deterministic behaviour.

- You can do the same intial setup -> 5-10 times -> same pipeline run -> 14*10 metrics 

- Then take standrd dev of these numbers

- Take noise threshold and keep it as 2*std dev

- So we say like there is a noise by llm so this is not regression

- Eg recall baseline=90, next result = 89.5

- metric_registry.py has details about metrics