import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Read data file
df = pd.read_csv("train.txt", sep=';', names=['text', 'emotion'])

# Build model
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000))
])

# Train model
model.fit(df['text'], df['emotion'])

# Save trained model
joblib.dump(model, 'emotion_model.pkl')

print("Model trained and saved as emotion_model.pkl")
