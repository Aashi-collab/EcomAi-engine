import json

def load_data():
    with open("app/data/products.json") as f:
        return json.load(f)

def get_all_products():
    return load_data()

def get_product_by_id(id):
    products = load_data()
    product = next((p for p in products if p["id"] == id), None)

    if not product:
        return {"error": "Product not found"}

    return product