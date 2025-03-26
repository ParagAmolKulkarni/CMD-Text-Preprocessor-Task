# CMD-Text-Preprocessor-Task

# CMD Text Preprocessor Task

A command-line text preprocessing and classification system with automatic environment configuration. Handles common NLTK/Python path issues and achieves **92% accuracy** on news article classification.

[![Python Version](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![NLTK Version](https://img.shields.io/badge/NLTK-3.8.1-green)](https://www.nltk.org/)

## Features
- ✅ Text cleaning pipeline:
  - Lowercasing
  - Special character removal
  - Tokenization
  - Stopword filtering
- 🚀 Built-in dataset (20 Newsgroups)
- 📊 Model evaluation metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
- 🔄 Automatic NLTK data handling

## Installation

1. **Clone Repository**

git clone https://github.com/ParagAmolKulkarni/CMD-Text-Preprocessor-Task.git
cd CMD-Text-Preprocessor-Task

## Install Dependencies
pip install -r requirements.txt
python -m pip install --force-reinstall nltk

#Download NLTK Resources
python -m nltk.download -d C:\Users\MONIKA\nltk_data punkt punkt_tab stopwords

#Run Training Pipeline
python train_model.py

Expected Output:
Sample Cleaned Text:
re car palio need new piston rings  
looking used copy tsr hockey game ibm pc contact  
probability virus infection via blood transfusion  

Accuracy: 0.92
Classification Report:
              precision    recall  f1-score   support
           0       0.93      0.91      0.92       198
           1       0.91      0.93      0.92       202

#File Structure
CMD-Text-Preprocessor-Task/
├── text_cleaner.py     # Text preprocessing logic
├── train_model.py      # Training pipeline
├── model.joblib        # Trained classifier (3.5KB)
├── tfidf.joblib        # TF-IDF vectorizer (15KB)
├── requirements.txt    # Dependency list
└── README.md           # This documentation


Common Issues

NLTK Resources Not Found:


# Set permanent NLTK path (Windows)
setx NLTK_DATA "%USERPROFILE%\nltk_data"
Module Not Found Errors:


# Force reinstall all dependencies
pip install --force-reinstall -r requirements.txt
VS Code Specific Issues:

Press Ctrl+Shift+P → "Python: Select Interpreter"



Process to input custom text into your program and get predictions:

#Custom Text Prediction
**Run with Command-Line Input**
```bash
python predict.py "Your text here with numbers 123 and symbols #@!"
```

Or Interactive Mode
```bash
python predict.py
```
# Then type/paste your text

Example Output
```bash
Cleaned Text: text numbers symbols
Predicted Class: Class 0
```

---

### **3. Workflow for Users**
1. **Train Model First** (One-Time)

```bash
python train_model.py
```
Make Predictions

```bash
# Single prediction
python predict.py "Heart disease risks in modern healthcare"
```
# Batch predictions (create a file later)
# (You can extend this as needed)

4. Input Handling Explained
Text Cleaning Pipeline:
```bash
Input: "COVID-19 VACCINE updates: 50% efficacy reported!"
Cleaned Text: ['covid', 'vaccine', 'updates', 'efficacy', 'reported']
```
Prediction Process:
Uses same TF-IDF vectorizer from training
Applies saved Logistic Regression model
Returns class (0 or 1) based on training categories

5. Supported Input Formats
Method	Example	Use Case
CLI Argument	python predict.py "Your text"	Quick single predictions
Interactive	python predict.py + type text	Multi-line inputs
File Input (Add Later)	python predict.py < input.txt	Batch processing

6. Error Handling
The script automatically:
Converts all text to lowercase
Removes special characters/numbers
Handles empty input
Verifies model files exist
Full Execution Demo

# Train first (if not done)
```bash
python train_model.py
```
```bash
# Test prediction
python predict.py "New graphics card with 8GB VRAM"
```
Output
```bash
Cleaned Text: new graphics card vram
Predicted Class: Class 0  # comp.graphics
```
