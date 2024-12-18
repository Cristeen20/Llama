from extract_content import content
prompt = f"""
You are an IELTS Writing examiner. Evaluate the following IELTS Writing Task 2 essay according to the official IELTS Writing Band Descriptors, which include:

1. **Task Achievement (TA)**: How well the writer addresses the task, including answering all parts of the question and providing a clear position.
2. **Coherence and Cohesion (CC)**: How logically ideas are organized and connected, including the use of paragraphing and linking words.
3. **Lexical Resource (LR)**: The range and accuracy of vocabulary used, including use of less common words and phrases.
4. **Grammatical Range and Accuracy (GRA)**: The variety and accuracy of sentence structures, grammar, and punctuation.

Essay to Evaluate:
{content}

Provide a detailed evaluation output in the following format:
- Task Achievement (Score: X/9): [Detailed feedback]
- Coherence and Cohesion (Score: X/9): [Detailed feedback]
- Lexical Resource (Score: X/9): [Detailed feedback]
- Grammatical Range and Accuracy (Score: X/9): [Detailed feedback]

Finally, give an **overall band score** and suggest two areas for improvement.
"""