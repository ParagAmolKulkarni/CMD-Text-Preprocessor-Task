from text_cleaner import TextCleaner
import joblib
import sys

# Load saved models
model = joblib.load('model.joblib')
tfidf = joblib.load('tfidf.joblib')

def predict_text(text):
    # Clean text
    cleaner = TextCleaner()
    cleaned_tokens = cleaner.clean_text(text)
    cleaned_text = ' '.join(cleaned_tokens)
    
    # Vectorize
    vectorized = tfidf.transform([cleaned_text])
    
    # Predict
    prediction = model.predict(vectorized)[0]
    return prediction, cleaned_text

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command-line input
        user_text = ' '.join(sys.argv[1:])
    else:
        # Interactive input
        user_text = input("Enter text to classify: ")
    
    pred, cleaned = predict_text(user_text)
    print("\nCleaned Text:", cleaned)
    print("Predicted Class:", "Class 0" if pred == 0 else "Class 1")