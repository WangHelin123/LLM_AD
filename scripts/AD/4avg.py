import json
from collections import defaultdict

# 1. Load the jsonl file
with open("/home/zunhao/zirui/LLaVA/playground/124data/124data_review_GPT_withoutoptions.jsonl", "r") as file:
    lines = file.readlines()

# 2. Initialize the score dictionary for each of the four questions
question_scores = defaultdict(list)

# 3. Process each entry in the data to get the scores for each specific question
for line in lines:
    data = json.loads(line)
    question_id = data["question_id"]
    specific_question_id = question_id % 4
    score = data["tuple"][0]
    
    question_scores[specific_question_id].append(score)

# 4. Calculate average score for each specific question
question_averages = {question_id: sum(scores) / len(scores) for question_id, scores in question_scores.items()}

# 5. Print the results
for question_id, avg_score in question_averages.items():
    print(f"Question {question_id + 1}: Average Score = {avg_score:.2f}")
