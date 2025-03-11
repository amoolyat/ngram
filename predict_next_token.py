import json
import random

def load_model(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def predict_next_token(model, context):
    context = tuple(context)
    if context in model["ngram_counts"]:
        next_tokens = model["ngram_counts"][context]
        return max(next_tokens, key=next_tokens.get)
    return random.choice(["public", "private", "int", "void", "return"])  # default fallback

if __name__ == "__main__":
    model = load_model("ngram_9.json")  # using 9-gram as the best model

    test_sentence = ["public", "static"]
    prediction = predict_next_token(model, test_sentence)
    print(f"Predicted next token: {prediction}")
