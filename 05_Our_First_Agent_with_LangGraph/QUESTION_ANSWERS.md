#### ❓ Question #1:

How does the model determine which tool to use?

ANSWER: The model determines which tool to use by analyzing the user’s message, comparing it to the available tools’ descriptions and capabilities, and then outputting a function call to the most appropriate tool as part of its response. This is handled internally by the model’s function-calling mechanism, which is designed to select and call tools in a way that best answers the user’s query.


#### ❓ Question #2:

Is there any specific limit to how many times we can cycle?

If not, how could we impose a limit to the number of cycles?

ANSWER: Based on Langchain documentation, there is a maximum default of "25 steps" - so our current code would hit that maximum number of steps then end.
To impose a custom limit, we can add logic to our conditional edge function (or state) to count the number of cycles/steps/messages, and return an "END" or stopping signal when our desired maximum is reached.


#### 🏗️ Activity #2:

Please write out the steps the agent took to arrive at the correct answer.

Parsed the query:
The agent recognized the user’s prompt required two separate tasks: searching ArXiv and finding authors’ latest tweets.

Searched ArXiv for QLoRA:
It used the arxiv tool to locate the QLoRA paper and retrieved the list of authors.

Extracted author names:
The agent parsed the ArXiv metadata to identify four authors associated with the paper.

Searched for tweets:
It used the tavily_search_results_json tool to search for each author’s latest tweet in parallel.

Compiled the final output:
The agent summarized and formatted the retrieved tweet data into a complete answer.


#### 🏗️ Activity #3:

Please create a dataset in the above format with at least 5 questions.

questions = [
    "What is the James Webb Space Telescope and when was it launched?",
    "Who was the first person to walk on the moon and when did it happen?",
    "What is the largest planet in our solar system?",
    "What is a black hole and how do they form?",
    "What is the current status of the Mars Perseverance rover?",
    "What are the main components of the International Space Station?"
]

answers = [
    {"must_mention" : ["James Webb", "2021"]},
    {"must_mention" : ["Neil Armstrong", "1969"]},
    {"must_mention" : ["Jupiter", "largest"]},
    {"must_mention" : ["gravity", "collapse"]},
    {"must_mention" : ["Mars", "rover"]},
    {"must_mention" : ["modules", "laboratory"]},
]


#### ❓ Question #3:

How are the correct answers associated with the questions?

ANSWER: The correct answers are associated with questions through positional indexing - the first question corresponds to the first answer, second question to second answer, etc. This is a simple but problematic approach because it's fragile to reordering, has no explicit linking, is error-prone, and difficult to maintain. A better approach would use dictionaries or structured formats with explicit associations.


#### ❓ Question #4:

What are some ways you could improve this metric as-is?

ANSWER: The current must_mention metric only does exact text matching and gives binary pass/fail scores. It could be improved by adding case-insensitive matching, fuzzy matching for typos, semantic similarity using embeddings, partial credit scoring, and context awareness to check if terms are used correctly. Major gaps include no semantic understanding of correctness, no fact verification, no completeness assessment, and no relevance scoring - it only checks for keyword presence rather than actual answer quality. The metric is too simplistic for meaningful evaluation of answer accuracy and comprehensiveness.



#### 🏗️ Activity #5:

Please write markdown for the following cells to explain what each is doing.

ANSWER: SEE NOTEBOOK.


#### 🏗️ Activity #4:

Please write what is happening in our `tool_call_or_helpful` function!

ANSWER: SEE NOTEBOOK.