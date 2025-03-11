# GenAI for Software Development (Ngram)

* [1) Introduction](#1-introduction)  
* [2) Getting Started](#2-getting-started)  
  * [2.1) Preparations](#21-preparations)  
  * [2.2) Install Packages](#22-install-packages)  
  * [2.3) Run N-gram](#23-run-n-gram-model)  
* [3) Report](#3-report)
* [4) Prepared Dataset](#4-resources)

# GenAI for Software Development: N-gram Code Completion

## **1. Introduction**
This project implements an **N-gram probabilistic language model** for **Java code completion**. The model predicts the next token in a sequence by learning probability distributions from training data and selecting the most likely next token. This technique is widely used in **natural language processing (NLP)** and **automated software development**.

---

## **2. Getting Started**
This project is implemented in **Python 3.9+** and is compatible with **macOS**.

### **2.1 Preparations**
#### Clone the repository:
```shell
$ git clone https://github.com/amoolyat/ngram.git
$ cd ngram
```

#### Set up a virtual environment:
For macOS/Linux:
```shell
$ python -m venv venv
$ source venv/bin/activate
```
To deactivate:
```shell
$ deactivate
```

For Windows:
```shell
$ python -m venv venv
$ venv\Scripts\activate
```
To deactivate:
```shell
$ deactivate
```

### **2.2 Install Packages**  
#### Install required dependencies:  
```shell
$ pip install -r requirements.txt
```

---

### **2.3 Run N-gram Model**  

#### **2.3.1. Prepare the Dataset**  
The dataset consists of tokenized Java methods stored in `train.txt`, `val.txt`, and `test.txt`.  
If starting from raw repositories (`repos.txt`), run the following commands:  

```shell
$ python clone_repos.py
$ python method_extraction.py
$ python cleaning.py
```

---

#### **2.3.2. Train the N-gram Model**  
Train an N-gram model using `train_ngram_model.py`:  

```shell
$ python train_ngram_model.py
```

This script learns token probabilities from `train.txt` and generates models for different N-values.  
The resulting model files are saved as:  
- `ngram_3.json`  
- `ngram_5.json`  
- `ngram_7.json`  
- `ngram_9.json`  

---

#### **2.3.3. Evaluate the Model**  
To assess model performance on the test set, run:  

```shell
$ python evaluate_model.py
```

Results will be stored in `results_student_model.json`.  
For comparison, instructor-provided results are in `results_teacher_model.json`.  

---

#### **2.3.4. Generate Predictions**  
To test the model on real Java snippets:  

```shell
$ python generate_predictions.py
```

Alternatively, use `predict_next_token.py` to predict the next token based on a given context:  

```shell
$ python predict_next_token.py
```
---

## **3. Report**

The assignment report is available in the file Assignment_Report.pdf.

## **4. Resources**

[Prepared Dataset](https://drive.google.com/drive/folders/1-V-YGsuiS_Z7D4K0XZExEqnqC9K9S8s_?usp=sharing)

## **4. Repository Structure**
```
📂 ngram/
 ├── 📁 java_repos/                 # Cloned Java repositories
 ├── 📄 clone_repos.py              # Script to clone repos
 ├── 📄 method_extraction.py        # Extracts Java methods
 ├── 📄 cleaning.py                 # Cleans & tokenizes data
 ├── 📄 train_ngram_model.json      # Trains N-gram model
 ├── 📄 predict_next_token.py       # Predicts next token
 ├── 📄 evaluate_model.py           # Evaluates model
 ├── 📄 requirements.txt            # Dependencies
 ├── 📄 results_teacher_model.json  # Teacher model results
 ├── 📄 results_student_model.json  # Student model results
 ├── 📄 README.md                   # Project documentation
```
---


