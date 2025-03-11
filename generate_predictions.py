import json
from collections import defaultdict

def load_model(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        model_data = json.load(f)
    n = model_data["n"]
    ngram_counts = {eval(k): v for k, v in model_data["ngram_counts"].items()}
    context_counts = {eval(k): v for k, v in model_data["context_counts"].items()}
    return n, ngram_counts, context_counts

def predict_next_token(context, ngram_counts, context_counts):
    if context in ngram_counts:
        next_token = max(ngram_counts[context], key=ngram_counts[context].get)
        return next_token, ngram_counts[context][next_token] / context_counts[context]
    return "<UNK>", 0  # Unknown token

def generate_predictions(model_file, test_file, output_file, num_samples=100):
    n, ngram_counts, context_counts = load_model(model_file)
    results = []
    
    with open(test_file, 'r', encoding='utf-8') as f:
        lines = [line.strip().split() for line in f.readlines()[:num_samples]]
    
    for tokens in lines:
        context = tuple(["<START>"] * (n - 1))
        generated = []
        
        for _ in range(len(tokens)):
            next_token, prob = predict_next_token(context, ngram_counts, context_counts)
            generated.append((next_token, prob))
            context = (*context[1:], next_token)
            if next_token == "<END>":
                break
        
        results.append({"original": tokens, "generated": generated})
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)
    
    print(f"Predictions saved to {output_file}")

if __name__ == "__main__":
    generate_predictions("ngram_9.json", "test.txt", "results_student_model.json")
