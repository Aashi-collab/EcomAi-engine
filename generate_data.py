from faker import Faker
import random, json

fake = Faker()

categories = ["electronics", "home", "beauty", "sports"]

products = []

for i in range(100):
    products.append({
        "id": i,
        "name": fake.word(),
        "category": random.choice(categories),
        "price": random.randint(100, 5000),
        "rating": round(random.uniform(1, 5), 1)
    })

with open("app/data/products.json", "w") as f:
    json.dump(products, f, indent=4)

print("dataset created")