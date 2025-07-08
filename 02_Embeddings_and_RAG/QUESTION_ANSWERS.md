#### ❓Question #1:

The default embedding dimension of `text-embedding-3-small` is 1536, as noted above. 

1. Is there any way to modify this dimension?
No, the dimension of text-embedding-3-small (which is 1536) cannot be modified manually. Each OpenAI embedding model has a fixed dimensionality defined by the architecture of the model itself. However, if you require a different embedding size, you can choose a different model — for example, text-embedding-3-large, which outputs 3072-dimensional vectors. While you can't directly customize the dimension of a specific model, selecting an alternative model gives you control over the dimensionality in that way.
2. What technique does OpenAI use to achieve this?
OpenAI uses transformer-based models to generate embeddings. When text is passed to the API, the model tokenizes the input and processes it through multiple transformer layers to produce a dense numerical vector. The result is a fixed-size embedding that captures the semantic meaning of the input text. These embeddings are designed so that similar texts produce similar vectors in the high-dimensional space. This technique enables powerful use cases like semantic search, classification, clustering, and recommendation by leveraging the spatial relationships between these vectors.


#### ❓Question #2:

What are the benefits of using an `async` approach to collecting our embeddings
Using an async approach to collecting embeddings allows the program to request and wait for multiple embedding results without blocking the entire execution of the application. This is particularly beneficial when working with APIs like OpenAI’s, where each request to generate an embedding can take some time due to network latency and processing. In a synchronous (sync) approach, each embedding call would wait until the previous one finishes, which can significantly slow down the program — especially when processing many documents. With async, multiple embedding requests can be made concurrently, and the program can continue handling other tasks while waiting for responses. This leads to much faster overall processing time and improved efficiency, especially in I/O-bound tasks like calling external APIs.

#### ❓ Question #3:

When calling the OpenAI API - are there any ways we can achieve more reproducible outputs?

To get more reproducible outputs from the OpenAI API, you can set a fixed seed value in your request. This controls the randomness in the generation process, so the same input and settings will consistently return the same output. It’s also important to keep parameters like temperature, top_p, and max_tokens fixed, as changes to these can affect the variability of the response. Using a seed alongside consistent generation settings is the best way to ensure stable and repeatable outputs.


#### ❓ Question #4:

What prompting strategies could you use to make the LLM have a more thoughtful, detailed response?

What is that strategy called?

Several prompting strategies can help an LLM produce more thoughtful and detailed responses:

Chain-of-Thought Prompting
This involves asking the model to “think step by step” before answering. By explicitly guiding it to explain its reasoning process, the model is more likely to produce logical, multi-step, and accurate responses.

Few-Shot Prompting
Providing a few examples of the kind of output you're expecting (e.g., questions + ideal answers) helps the model understand the format, depth, and reasoning style you want it to follow.

Instructional Prompting
Using clear and explicit instructions in your prompt (e.g., “Explain in detail why…”, “List and describe…”, “Summarize this as if explaining to a beginner”) increases the likelihood of receiving detailed and focused responses.

The strategy that specifically encourages detailed reasoning by asking the model to walk through its thought process is called Chain-of-Thought Prompting.

