# Questions and Answers

## Question 1: RAG Text Splitter
**What is the purpose of the `chunk_overlap` parameter when using `RecursiveCharacterTextSplitter` to prepare documents for RAG, and what trade-offs arise as you increase or decrease its value?**

**Answer:** The `chunk_overlap` parameter controls how much text is shared between consecutive chunks. Increasing overlap improves context continuity and helps maintain relationships between concepts across chunk boundaries, but increases storage and processing costs. Decreasing overlap reduces redundancy but may lose important context connections. This is particularly important for maintaining semantic coherence when splitting long documents or preserving key phrases that span chunk boundaries.

## Question 2: Retriever Configuration
**Your retriever is configured with `search_kwargs={"k": 5}`. How would adjusting `k` likely affect RAGAS metrics such as Context Precision and Context Recall in practice, and why?**

**Answer:** Increasing `k` improves Context Recall by retrieving more potentially relevant documents, but may decrease Context Precision by including less relevant documents. Decreasing `k` improves precision by focusing on top results but may miss relevant context, reducing recall. The optimal `k` balances these trade-offs based on the specific use case. For fact-finding tasks, higher `k` values are often preferred, while for summarization tasks, lower `k` values may be more appropriate.

## Question 3: LangGraph Assistants
**Compare the `agent` and `agent_with_helpfulness` assistants defined in `langgraph.json`. Where does the helpfulness evaluator fit in the graph, and under what condition should execution route back to the agent vs. terminate?**

**Answer:** The `agent_with_helpfulness` adds a helpfulness evaluation node that assesses response quality. If the response is deemed unhelpful, execution routes back to the agent for improvement. If the response meets helpfulness criteria, execution terminates. This creates a feedback loop for quality assurance compared to the simple `agent` which executes once and terminates. The helpfulness evaluator typically uses criteria like relevance, completeness, and clarity to determine whether a response adequately addresses the user's query.
