from fastapi import APIRouter, HTTPException
from typing import List
from app.models.products_model import Product
from app.services.ml_service import recommend_products

router = APIRouter()

@router.get("/recommend/{id}", response_model=List[Product])
def recommend(id: int):
    result = recommend_products(id)

    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result