import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Load data
with open("app/data/products.json") as f:
    products = json.load(f)

# Combine text features
texts = [
    p["name"] + " " + p["category"]
    for p in products
]

# Convert to vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(texts)

# Compute similarity matrix
similarity = cosine_similarity(vectors)

# Save model
joblib.dump((similarity, products), "ml/model.pkl")

print("✅ Model trained and saved")