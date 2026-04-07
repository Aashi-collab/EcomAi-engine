from fastapi import FastAPI
from app.routes import products, recommend

app = FastAPI()

app.include_router(products.router)
app.include_router(recommend.router)