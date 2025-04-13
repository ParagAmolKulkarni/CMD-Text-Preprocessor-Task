Here’s your **fully updated `README.md`** – clean, Jupyter-Notebook based, and perfectly tailored for your new structure:

---

# CMD-Text-Preprocessor-Task

A **command-line-compatible** and **Jupyter-based** text preprocessing and classification system with automatic environment setup and **92% accuracy** on news article classification.

[![Python Version](https://img.shields.io/badge/Python-3.08-blue)](https://www.python.org/)  
[![NLTK Version](https://img.shields.io/badge/NLTK-3.8.1-green)](https://www.nltk.org/)

---

## 🚀 Features

- ✅ Text preprocessing pipeline:
  - Lowercasing
  - Special character & number removal
  - Tokenization
  - Stopword filtering
- 📦 Built-in dataset (20 Newsgroups)
- 📈 Metrics:
  - Accuracy
  - Precision, Recall
  - F1-Score
- 🔄 Automatic NLTK data handling
- 💬 User input-based predictions inside notebook
- 🧠 Achieves ~92% model accuracy

---

## 📁 File Structure

```
CMD-Text-Preprocessor-Task/
├── text_cleaner.py         # Core text cleaning functions
├── train_model.ipynb       # Training pipeline notebook
├── predict.ipynb           # Input and prediction notebook
├── model.joblib            # Trained logistic regression model
├── tfidf.joblib            # TF-IDF vectorizer
├── requirements.txt        # All dependencies
└── README.md               # This file
```

---

## ⚙️ Setup Instructions

### 1. 📥 Clone the Repo

```bash
git clone https://github.com/ParagAmolKulkarni/CMD-Text-Preprocessor-Task.git
cd CMD-Text-Preprocessor-Task
```

---

### 2. 📦 Install Dependencies

```bash
pip install -r requirements.txt
python -m pip install --force-reinstall nltk
```

---

### 3. 🔄 Download Required NLTK Resources

```bash
python -m nltk.downloader -d C:\Users\<YourUsername>\nltk_data punkt stopwords
```

Replace `<YourUsername>` accordingly.

If you want to permanently set the path:

```bash
setx NLTK_DATA "%USERPROFILE%\nltk_data"
```

---

## 🧪 Training the Model

Open **`train_model.ipynb`** using Jupyter or VS Code:

```bash
jupyter notebook
```

➡️ Run all the cells to:
- Preprocess sample text
- Train the model using 20 Newsgroups data
- Save the model (`model.joblib`) and vectorizer (`tfidf.joblib`)

✅ Expected Output:
```
Sample Cleaned Text:
re car palio need new piston rings  
looking used copy tsr hockey game ibm pc contact  
probability virus infection via blood transfusion

Accuracy: 0.92
Classification Report:
              precision    recall  f1-score   support
           0       0.93      0.91      0.92       198
           1       0.91      0.93      0.92       202
```

---

## 🔍 Making Predictions

Open **`predict.ipynb`** using Jupyter Notebook or VS Code.

➡️ You can:
- Enter a custom input inside `input()` prompt
- Or modify the variable `user_text` directly to auto-predict specific strings

### Example:

```python
Input: "New NVIDIA graphics card with 8GB VRAM and ray tracing"
Output:
Cleaned Text: new nvidia graphics card vram ray tracing  
Predicted Class: Class 0  # (e.g., comp.graphics)
```

---

## 🧠 Text Cleaning Pipeline Overview

### Input
```text
"COVID-19 VACCINE updates: 50% efficacy reported!"
```

### After Cleaning
```text
['covid', 'vaccine', 'updates', 'efficacy', 'reported']
```

---

## 📤 Supported Input Modes

| Method         | Example                                      | Use Case               |
|----------------|----------------------------------------------|------------------------|
| Manual Input   | Run `predict.ipynb` & enter text via prompt  | Custom predictions     |
| Hardcoded Text | Modify `user_text` variable in notebook      | Quick tests or demos   |
| File Input     | *(Extendable)* - Future feature for batch    | Multiple inputs later  |

---

## 🛠 Troubleshooting

### NLTK Resources Not Found?

Run:

```bash
python -m nltk.downloader -d C:\Users\<YourUsername>\nltk_data punkt stopwords
```

Or set path permanently:

```bash
setx NLTK_DATA "%USERPROFILE%\nltk_data"
```

---

## ✅ Workflow Summary

### 1. Train the Model (first time only)

```bash
jupyter notebook
# Open train_model.ipynb and run all cells
```

### 2. Make Predictions

```bash
# Open predict.ipynb and run the input cell
```

---

## 🧠 Model Insights

- TF-IDF vectorizer helps map word importance
- Logistic Regression classifier trained on 2-class subset of 20 Newsgroups
- You can easily swap in your own dataset

---

## 🔧 Future Extensions

- Batch input from file
- Add GUI via Flask or Gradio
- Expand to multi-class classification

---
