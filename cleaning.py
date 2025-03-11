import os
import random
import re
from sklearn.model_selection import train_test_split

def load_methods(file_path):
    try:
        with open(file_path, 'r') as file:
            methods = file.readlines()
        print(f"Loaded {len(methods)} methods from {file_path}.")
        return [method.strip() for method in methods if method.strip()]  
    except Exception as e:
        print(f"Error loading methods: {e}")
        return []

def tokenize_methods(methods):
    tokenized_methods = []
    try:
        for method in methods:
            tokens = re.findall(r'\b\w+\b', method)
            if tokens:
                tokenized_methods.append(tokens)
            else:
                print(f"Skipping empty or invalid method: {method}")
        print(f"Tokenized {len(tokenized_methods)} methods.")
    except Exception as e:
        print(f"Error tokenizing methods: {e}")
    return tokenized_methods

def split_dataset(data, test_size=0.2, val_size=0.1):
    try:
        if len(data) == 0:
            print("No methods to split, exiting.")
            return [], [], []

        train, temp = train_test_split(data, test_size=test_size + val_size, random_state=42)
        
        val, test = train_test_split(temp, test_size=0.5, random_state=42)

        print(f"Dataset split: {len(train)} train, {len(val)} val, {len(test)} test.")
        return train, val, test
    except Exception as e:
        print(f"Error splitting dataset: {e}")
        return [], [], []
        
def save_data(data, filename):
    try:
        with open(filename, 'w') as file:
            for method in data:
                file.write(' '.join(method) + '\n')  # Save each method as a space-separated line
        print(f"Saved {len(data)} methods to {filename}.")
    except Exception as e:
        print(f"Error saving data: {e}")

#  main function to process methods
def process_methods(input_file):
    methods = load_methods(input_file)
    if not methods:
        return

    # tokenize methods
    tokenized_methods = tokenize_methods(methods)
    if not tokenized_methods:
        return

    # split dataset into train, validation, and test sets
    train, val, test = split_dataset(tokenized_methods)

    save_data(train, 'train.txt')
    save_data(val, 'val.txt')
    save_data(test, 'test.txt')

    print(f"Processed {len(train)} train, {len(val)} val, {len(test)} test methods.")

# run process
if __name__ == '__main__':
    input_file = 'java_methods.txt'  
    process_methods(input_file)
