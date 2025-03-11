import javalang
import os

def extract_methods_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    methods = []
    try:
        tree = javalang.parse.parse(code)
        for _, node in tree.filter(javalang.tree.MethodDeclaration):
            methods.append(str(node))  # using str() instead of to_string()
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    return methods

def extract_from_directory(directory):
    all_methods = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                all_methods.extend(extract_methods_from_file(file_path))
    return all_methods

# usage:
java_methods = extract_from_directory("/Users/strawberry/eclipse-workspace/ngram/java_repos")
print(f"Extracted {len(java_methods)} methods")

# saving to a text file and handling certain problematic characters (ran into errors such as '#')
with open("java_methods.txt", "w", encoding="utf-8", errors="ignore") as f:
    for method in java_methods:
        f.write(method + "\n")

