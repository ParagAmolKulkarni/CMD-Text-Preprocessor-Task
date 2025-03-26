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

bash
Copy
# Set permanent NLTK path (Windows)
setx NLTK_DATA "%USERPROFILE%\nltk_data"
Module Not Found Errors:

bash
Copy
# Force reinstall all dependencies
pip install --force-reinstall -r requirements.txt
VS Code Specific Issues:

Press Ctrl+Shift+P → "Python: Select Interpreter"




