def evaluate_sheet(detected_bubbles, answer_key):
    # Placeholder: for now assume detected answers match answer key
    results = {}
    for i, ans in enumerate(answer_key):
        results[f"Q{i+1}"] = ans
    score = len(answer_key)
    return {"answers": results, "score": score}
