from ngram_model import NGramModel

n_values = [3, 5, 7, 9]
for n in n_values:
    model = NGramModel(n)
    model.train("train.txt")
    model.save_model(f"ngram_{n}.json")
    print(f"{n}-gram model trained and saved.")
