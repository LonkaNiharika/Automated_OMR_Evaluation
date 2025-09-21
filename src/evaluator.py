import json

def evaluate(detected_answers, answer_key_path):
    with open(answer_key_path, "r") as f:
        answer_key = json.load(f)
    score = 0
    for q, ans in detected_answers.items():
        if ans == answer_key.get(q):
            score += 1
    return score
