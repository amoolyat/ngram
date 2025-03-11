import json
import math

def load_model(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        model_data = json.load(f)
    return model_data

def compute_perplexity(model, file):
    n = model["n"]
    ngram_counts = {eval(k): v for k, v in model["ngram_counts"].items()}
    context_counts = {eval(k): v for k, v in model["context_counts"].items()}
    
    total_log_prob = 0
    total_tokens = 0

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            tokens = ["<START>"] * (n - 1) + line.strip().split() + ["<END>"]
            for i in range(len(tokens) - n + 1):
                context = tuple(tokens[i:i + n - 1])
                token = tokens[i + n - 1]
                prob = ngram_counts.get(context, {}).get(token, 1e-10) / context_counts.get(context, 1e-10)
                total_log_prob += math.log(prob)
                total_tokens += 1

    perplexity = math.exp(-total_log_prob / total_tokens)
    return perplexity

if __name__ == "__main__":
    test_file = "test.txt"  # replace with val.txt for validation
    
    for n in [3, 5, 9]:
        model = load_model(f"ngram_{n}.json")
        perplexity = compute_perplexity(model, test_file)
        print(f"Perplexity for {n}-gram model: {perplexity:.4f}")
