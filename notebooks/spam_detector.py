import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# Load real SMS Spam Collection dataset
df = pd.read_csv(
    "notebooks/dataset/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

print("Dataset loaded successfully!")
print("Total messages:", len(df))


# Separate input and output
X = df["message"]
y = df["label"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create machine learning pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])


# Train model
model.fit(X_train, y_train)
joblib.dump(model, "spam_model.pkl")
print("Model saved successfully!")

print("Model training completed!")


# Test model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)


# Test new messages
test_messages = [
    "Congratulations! You won a free iPhone!",
    "Hey, can you send me today's class notes?",
    "URGENT! Claim your cash prize now!"
]

results = model.predict(test_messages)


print("\n--- Prediction Results ---")

for message, result in zip(test_messages, results):
    print("\nMessage:", message)
    print("Prediction:", result)