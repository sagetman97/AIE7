##### ❓ Question #1:

Why is a "powerful" LLM important for this use-case?

What tasks must our Agent perform that make it such that the LLM's reasoning capability is a potential limiter?

ANSWER: A powerful LLM is crucial for this use-case because the multi-agent RAG system must perform complex reasoning, synthesize information from diverse and often technical sources, and coordinate multiple specialized agents to answer nuanced user queries. The agents are required to interpret and break down complex questions, route tasks appropriately, and generate clear, contextually accurate, and well-structured responses, often by leveraging external tools and adhering to strict output schemas. Without strong reasoning capabilities, a weaker LLM would struggle to understand context, misroute tasks, fail to synthesize or summarize long documents, and produce generic or incorrect outputs, ultimately limiting the system’s effectiveness in delivering high-quality, relevant, and reliable answers.

##### 🏗️ Activity #2:

Using whatever drawing application you wish - please label the flow above on a diagram of your graph.

ANSWER: SEE Multi_Agent_RAG_LangGraph.ipynb. Chromium used to create visual diagram. 



##### ❓ Question #2:

How could you make sure your Agent uses specific tools that you wish it to use? Are there any ways to concretely set a flow through tools?

ANSWER: To make sure my Agent uses specific tools and follows a desired flow, I can adjust the agent’s prompt to instruct it to use certain tools for specific tasks, and I can implement explicit if/then logic in my orchestration code to route requests to the right tool or agent based on conditions. I can also bind only the tools I want each agent to use, so they can’t access others. By using a supervisor or router agent, I can control which sub-agent (and thus which tool) is called at each step. Finally, I can define a workflow or state graph that enforces the allowed sequence of tool usage. By combining prompt engineering, conditional logic, tool binding, supervisor routing, and workflow graphs, I can achieve both flexible and strictly controlled tool usage in my multi-agent system.


##### 🏗️ Activity #3:

Describe, briefly, what each of these tools is doing in your own words.

ANSWER:
create_outline:
This tool lets me create an outline by taking a list of main points or sections and saving them as a numbered list in a text file. I specify the points and the file name, and it writes each point as a separate line in the file.

read_document:
With this tool, I can read the contents of a document from a file in my working directory. I can also specify which lines I want to read by providing start and end line numbers, making it easy to extract just a portion of the document if needed.

write_document:
This tool allows me to write any text content I want into a new or existing file. I provide the content and the file name, and it saves the text to that file for later use or reference.

reference_previous_responses:
This tool helps me look up previous responses that are relevant to a specific query. I enter a search query, and it searches a database of past responses (using a retriever) to find matches, which is useful for referencing earlier work or avoiding repetition.

edit_document:
With this tool, I can edit an existing document by inserting new text at specific line numbers. I provide a dictionary where each key is a line number and each value is the text to insert at that spot. The tool updates the file with my changes and saves it.