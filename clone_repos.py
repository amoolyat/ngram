import os
import subprocess

REPO_DIR = "java_repos"

# creates the folder if it doesn’t exist
if not os.path.exists(REPO_DIR):
    os.makedirs(REPO_DIR)

with open("repos.txt", "r") as f:
    repos = f.readlines()

for repo in repos:
    repo = repo.strip()
    if repo:
        repo_name = repo.split("/")[-1].replace(".git", "")
        repo_path = os.path.join(REPO_DIR, repo_name)
        
        if not os.path.exists(repo_path):  # to avoid downloading the same repo twice
            print(f"Cloning {repo}...")
            subprocess.run(["git", "clone", repo, repo_path])
        else:
            print(f"Skipping {repo}, already downloaded.")