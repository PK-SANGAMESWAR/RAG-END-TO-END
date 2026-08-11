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

## But this is a bad idea - as you have correct - doc id or chunk id to evaluate

Change in document content can make chnge in id
So think, we have many chunks -> len(chunks) = 800+, if the man whom we gave task to create golden dataset -> it would be very difficult -> Also improvement or any chnge in hyperaparam of chunking would  chnge the chunks -> have to regenerate chunks in VectorDB and so again make goldens 

If chunking params dont chnge and chunk size dont chnge use the above id trick this is not an issue

## So, creation of golden dataset (question and ideal ans(from vector db))

question                         Ideal ans made by combinied the answers in chunk id               
what is regression Testing?   
What is RAG Triad?
....


## How to calculate recall and precision

retiever <- Question (Searches for contexts) = 72, 81,89, 99, 100

LLM as a judge -> give ideal ans and tell it "break into claims"

Go to each claim and tell which of the three claims exist in the context chunk id extracted 

Say we get all the claims in 72, 81,89, 99, 100

So we get recall = 1

## Say you increase chunk size -> no neeed to make chnegs in golden dataset = This is called contextual Recall which uses llm as judge

Precision = question -> retiever - 72, 81, 89, 99,100

LLM as a judge <- Go to each chunk and check if content in chunk answers the question

Precision also considers rank of retrieved chunks
There may be diff in precision if rank chnges 

But Normal precision treats both as same and give same ans

Use [Contextual Precision]


## Retrieval Golden Dataset

1. Hand Authored
2. LLM assisted drafting and human review
3. DeepEval synthesizer and Human review
4. Production log mining

We try to use DeepEval but got bad results

So we proceeded to do with LLM based @retiever_goldens.json (15 questions)


## Make chnges in chunking params and again run for increase precision and recall

We ll get new baseline

## Precision -> Implement reranker 

## For more improvement -> use diff embedding model -> May be use large 

## May be decrease k -> try to increase precision 

## May be use a diff reranker as we have used basic reranker