##### ❓ Question #1:
What is the embedding dimension, given that we're using `text-embedding-3-small`?
You will need to fill the next cell out correctly with your embedding dimension for the rest of the notebook to run.
> HINT: Check out the docs to help you answer this question.

ANSWER: embedding_dim = 1536


#### ❓ Question #2:
LangGraph's graph-based approach lets us visualize and manage complex flows naturally. How could we extend our current implementation to handle edge cases? For example:
- What if the retriever finds no relevant context?  
- What if the response needs fact-checking?
Consider how you would modify the graph to handle these scenarios.

Answer: To robustly handle edge cases in a LangGraph-based RAG system, you can enhance the graph by introducing a conditional node immediately after the retrieval step that inspects whether any relevant context was found; if the retriever returns no documents, the workflow is directed to a fallback node that gracefully informs the user that no relevant information is available, ensuring a better user experience. Furthermore, after the generation step, you can add a fact-checking node that programmatically or via an additional LLM prompt verifies the factual accuracy of the generated response; if the answer is validated, it proceeds to the user, but if it fails the check, the system can automatically append a disclaimer or suggest consulting an expert. By leveraging LangGraph’s ability to branch and compose nodes based on state, this design allows your RAG application to dynamically adapt to missing context and the need for answer verification, resulting in a more reliable and user-friendly system.


LANGSMITH:
#### ❓Question #1:

What conclusions can you draw about the above results?
Describe in your own words what the metrics are expressing.

ANSWER:
Looking over the results, it’s clear the RAG system is pulling its weight—most answers are right on target and closely echo the reference responses, as shown by those high “score_string” marks and the abundance of “correct” flags. The system is also quite efficient, cranking out answers in a flash and keeping costs to a bare minimum. However, the “dopeness” metric suggests that, while the responses are accurate, they might benefit from a bit more spark or originality to make them pop. Altogether, these metrics paint a pretty comprehensive picture of how things are running: you get a sense of precision, operational efficiency, and the overall vibe of the answers, which is super useful for deciding what to fine-tune next.

Cot Context: This stat reflects how many context snippets or reasoning hops the model leans on for each answer. A steady 1.00 means it’s usually sticking to a single, relevant chunk—no unnecessary detours.
Dopeness: Here’s a fun one—it checks if the answer isn’t just correct, but also has some pizzazz. It’s a simple yes/no, and the lower average hints that while the system is reliable, it could stand to be a bit more lively.
Score_string: Rated out of 10, this shows how tightly the output matches the gold-standard answer, as judged by another language model. Lots of 9s and 10s mean it’s hitting the mark.
Latency: This is all about speed—most answers are delivered promptly, so the system isn’t bogged down.
Completed: Just a status check to confirm each evaluation wrapped up as expected.
Tokens: This tracks how much text the model processes per question, which is handy for monitoring resource consumption.
Cost: Reflects the expense per query, and the numbers are so low you’d barely notice them.
