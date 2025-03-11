import json
from collections import defaultdict

class NGramModel:
    def __init__(self, n):
        self.n = n
        self.ngram_counts = defaultdict(lambda: defaultdict(int))
        self.context_counts = defaultdict(int)

    def train(self, file):
        """Train the N-gram model from a text file."""
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                tokens = ["<START>"] * (self.n - 1) + line.strip().split() + ["<END>"]
                for i in range(len(tokens) - self.n + 1):
                    context = tuple(tokens[i:i + self.n - 1])
                    next_token = tokens[i + self.n - 1]
                    self.ngram_counts[context][next_token] += 1
                    self.context_counts[context] += 1

    def get_probability(self, context, token):
        """Returns probability of a token given a context."""
        return self.ngram_counts[context][token] / self.context_counts[context] if self.context_counts[context] > 0 else 0

    def save_model(self, filename):
        """Save the trained N-gram model as a JSON file."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                "n": self.n,
                "ngram_counts": {str(k): v for k, v in self.ngram_counts.items()},
                "context_counts": {str(k): v for k, v in self.context_counts.items()}
            }, f, indent=4)

if __name__ == "__main__":
    # Train 3-gram, 5-gram, and 9-gram models
    for n in [3, 5, 7, 9]:
        model = NGramModel(n)
        model.train("train.txt")
        model.save_model(f"ngram_{n}.json")
        print(f"{n}-gram model trained and saved.")
