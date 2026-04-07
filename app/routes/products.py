from fastapi import APIRouter, Query, HTTPException
from typing import List
from app.services.product_service import get_all_products, get_product_by_id
from app.models.products_model import Product

router = APIRouter()

@router.get("/products", response_model=List[Product])
def get_products(
    category: str = None,
    min_price: int = None,
    max_price: int = None
):
    products = get_all_products()

    if category:
        products = [p for p in products if p["category"].lower() == category.lower()]

    if min_price is not None:
        products = [p for p in products if p["price"] >= min_price]

    if max_price is not None:
        products = [p for p in products if p["price"] <= max_price]

    return products


@router.get("/products/{id}", response_model=Product)
def get_product(id: int):
    product = get_product_by_id(id)

    if "error" in product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.get("/search", response_model=List[Product])
def search_products(q: str = Query(...)):
    products = get_all_products()
    return [p for p in products if q.lower() in p["name"].lower()]