ANSWERS:


FIRST ATTEMPT:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner. 
    - Aspect Tested: This checks whether the chatbot can explain complex programming concepts in a simplified and beginner-friendly way. The goal is to assess how well it adapts its tone, structure, and analogies to suit someone with no prior coding knowledge. The explanation uses terms like “methods” and “attributes” without defining them clearly, which could confuse a beginner. It might help to improve prompt instructions to encourage simpler language and analogies. Adding markdown formatting (e.g., bold key terms) could also make the explanation easier to follow.
2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: This prompt tests the chatbot’s ability to distill a long, nuanced passage into a short, coherent summary that captures the most critical information. It evaluates comprehension, prioritization of ideas, and clarity of expression. The summary misses a few important points and reuses some original phrasing rather than rewording. I might improve prompt instructions to emphasize the need for abstraction and clearer, rephrased output. It could also benefit from formatting support to break ideas into separate lines or bullets.
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: This prompt tests the model’s ability to generate creative and coherent narrative text. It evaluates storytelling skills, emotional tone, imagination, and the ability to stay within length constraints while maintaining engagement. The story feels a bit rushed and lacks a clear structure. It might help to add prompt instructions that guide the model, while staying within word limits. Supporting line breaks and formatting would make it more readable as well.
4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: This prompt tests the model’s ability to apply basic arithmetic and logical reasoning to solve a constrained word problem. It evaluates accuracy, step-by-step problem solving, and understanding of unit relationships. The model gives the correct answer but skips over the reasoning. It could be useful to prompt it to show its thought process step-by-step. Also, formatting the logic in a clearer way (e.g., numbered steps or line breaks) might improve readability.
5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: This prompt tests the model’s ability to adjust tone and style—specifically, transforming informal or casual language into a professional and formal register. It evaluates linguistic flexibility, audience awareness, and tone control. The tone is improved but still slightly casual in places. I might adjust the prompt to make the tone expectations more explicit and support clearer formatting to distinguish the rewritten version.


SECOND ATTEMPT AFTER ENHANCEMENTS:

 1. Explain the concept of object-oriented programming
Post-Enhancement Evaluation:
The explanation is now much easier to understand, with simplified language and a real-world analogy. Markdown formatting (e.g., bolding key terms like objects and methods) makes the content more readable. Improved prompt instructions also help steer the explanation toward a beginner-friendly tone.

2. Summarize a long paragraph
Post-Enhancement Evaluation:
The summary is more focused and avoids copying full sentences from the original text. Prompt instructions help the model prioritize key points, and the formatting (e.g., line breaks between ideas) improves clarity. It captures both the main idea and supporting concerns more reliably.

3. Write a short, imaginative story
Post-Enhancement Evaluation:
The story now stays within the word limit and has a clearer structure, including a defined setting and resolution. The tone feels more expressive, and markdown formatting adds readability. Prompt guidance seems to help it balance creativity with coherence.

4. Solve a math word problem
Post-Enhancement Evaluation:
The model now shows its work step-by-step before arriving at the final answer. The reasoning is clearer thanks to prompt improvements, and markdown formatting (e.g., numbered steps or line breaks) makes the explanation easier to follow.

5. Rewrite in a professional tone
Post-Enhancement Evaluation:
The rewrite now fully adopts a formal tone, removing all casual phrases and presenting a polished message. Prompt instructions about tone and audience seem to be working well. The formatting also helps visually separate the rewritten paragraph from the original.

##### 🧑‍🤝‍🧑❓ Discussion Question #1:

Vibe checking offers a quick and informal way to gauge whether an LLM application is functioning at a basic level, but it falls short as a reliable evaluation method. Its most significant limitation is subjectivity: results depend heavily on individual interpretation, which can vary based on the tester's expectations, experience, or familiarity with the task. This makes it difficult to compare performance across users or over time.

Another drawback is its lack of structure. Vibe checks typically don't involve predefined metrics, datasets, or scenarios, which makes it hard to quantify system accuracy, consistency, or robustness. They also tend to focus on general impressions, which may overlook deeper issues like factual errors, ethical failures, or poor performance on edge cases.

Because it provides limited diagnostic feedback, vibe checking is best suited for identifying major breakdowns in early prototypes. For production-ready systems or nuanced tasks, it should be paired with more formal evaluations — such as unit tests, benchmark datasets, or human rating — that offer measurable and repeatable results aligned with the intended use case.

