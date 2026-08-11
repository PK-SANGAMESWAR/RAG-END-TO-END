## Setting up the project

1. Create new folder - rag eval
2. Create dir structure
3. Add transcripts
4. Create env
5. Install dependencies
5. Create .env files

These are done

## Build the retriever 

Component which gets query and convert into vector using embed model and search in the vector db where chunks are present using the query vector 

Load transcripts -> Load and reads line by line and check if there are any time stamps if no add to docs (only txt are used) -> doc objects and we have meta data of which session the transcriptt is told

use an embedding model - text-embedding-3-small
save in chromadb with chunk_size = 1000 and overlap 150 

build retriever and make object 

## Evaluate the Retriever

Failure mode ->  Miss of chunks taken, Noise which has non related chunks + correct chunks

Metrics -> recall@k, precision

recall -> out of all context how much retriever took
precision-> out of produced chunks by retriever which all are correct and useful

Increasing k increase recall but precision gets lower, so we have a tradeoff bw both

So to evaluate recall and precision - Both recall and precision are reference-based evaluations [Because you have to have a golden dataset prior].

## Create Golden dataset

question                      Chunk id
What is regression testing    72, 89, 100
What is RAG Triad             120, 111
What are online evals         151, 121, 130
....
....

Give each question to retriever -> suppose it took 72, 82, 89, 99, 100 

recall = 3/3 = 1
...For each question and take avg -> Avg recall value

Give each question to retriever -> suppose it took 72, 82, 89, 99, 100 

precision = 3/5 
...For each question and take avg -> Avg precision value




