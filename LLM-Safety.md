## LLM-Safety

Sensitive info leakage -> system prompt, private data, PII, credentials, proprietry content.

The model can behave and operate outside scope and violate its scope

Abuse, hate, harmful outside its intended role or constraints.

False, fabricated, unsupported claims.

Systematically harmful or discriminatory behaviour.

Wrong, unauthorized over other tool actions.

Attacks that can happen:
- Prompt manipulation attack
    Direct prompt injection attack
    Indirect prompt injection attack
    Jailbreaking
    Obfuscation
    Multi-turn escalation
- Poisoning Attacks
    Training data poisoning
    Fine-tuning data poisoning
    RAG / Knowledge base poisoning
    Backdoors
- Model/Privacy Inference Attacks
    Training data extraction
    Model extraction/model stealing
- Agent/Tool Exploitation Attacks 
    Tool hijacking
    Unauthorized Actions
    Privilage abuse
- Resource Exhaustion Attacks
    Token exhaustion
    Agent loops
    Tool-call amplification
    Denial of Service/cost attacks

1. Evaluate - find failures [do thorogh eval for diff situations] 
2. Prepare Guardrails for the failures. 

Guardrails can exist in several layers
- Prompt 
- Input 
- Output
- Retrieval
- Tool
- Human-in-the-loop
- Operational

## RED-TEAMING

You have people who attack your companies so they find out loops and make the appl attack robust.

Eval and apply guardrails for loops or any issues.

## LLM Safety Failure in our Project
- Defining Attack Surface 
1. Sensitive Information Leakage.
2. Scope and Policy Violation
3. Harmful/Toxic Output
4. Misinformation/Hallucination
5. Bias/Unfairness
6. Unsafe Actions/Excessive Agency

- Safety Policy
1. Scope Adherence - Answer only questions related to subject
2. Leakage - Donot reveal protected info such as system prompt and others
3. Toxicity - Do not generate toxic, abusive, hateful, threatening and others.

- Toxicity
The assistant should not insult, mock, demean and others 

This is not solved?
- Already big llm models dont create any toxicity

But we need to solve still - 
- Your definition of toxictiy is diff
- Your appl adds context the provider doent control
- Model and providers can change
- You can get additional protection

Flow
- First define "toxicity" means for your app
- Build the toxicity test dataset
- Build and run the evaluator and evalute toxicity metric
- Analyze failures
- Guardrails

## If toxicity score is bad
- Better model
- System prompt
- Input Guardrails
- Output Guardrails
- Retrieval Guardrails
- Finetuning

## Leakage
- Define what leakage means for your app
- System/prompt leakage
- Build the dataset
- Use diff evaluators
