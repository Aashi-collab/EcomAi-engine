import joblib

# Load model once
similarity, products = joblib.load("ml/model.pkl")

def recommend_products(product_id: int):
    # Find index
    index = next((i for i, p in enumerate(products) if p["id"] == product_id), None)

    if index is None:
        return {"error": "Product not found"}

    # Get similarity scores
    scores = list(enumerate(similarity[index]))

    # Sort by similarity
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Skip first (itself)
    top = scores[1:6]

    # Return products
    return [products[i] for i, _ in top]