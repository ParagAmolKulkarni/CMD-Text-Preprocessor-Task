from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from text_cleaner import TextCleaner
import pandas as pd
import joblib

# Load built-in dataset
categories = ['rec.sport.baseball', 'sci.med']
newsgroups = fetch_20newsgroups(subset='all', categories=categories)

# Create DataFrame
df = pd.DataFrame({
    'text': newsgroups.data,
    'label': newsgroups.target
})

# Clean text
cleaner = TextCleaner()
df['cleaned'] = df['text'].apply(lambda x: ' '.join(cleaner.clean_text(x)))

# Display sample cleaned text
print("\nSample Cleaned Text:")
print(df['cleaned'].head(3).to_string(index=False))

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    df['cleaned'], df['label'], test_size=0.2, random_state=42
)

# Vectorization
tfidf = TfidfVectorizer(max_features=1000)
X_train_tf = tfidf.fit_transform(X_train)
X_test_tf = tfidf.transform(X_test)

# Model training
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tf, y_train)

# Save models
joblib.dump(model, 'model.joblib')
joblib.dump(tfidf, 'tfidf.joblib')

# Evaluation
preds = model.predict(X_test_tf)
print(f"\nAccuracy: {accuracy_score(y_test, preds):.2f}")
print("Classification Report:")
print(classification_report(y_test, preds))