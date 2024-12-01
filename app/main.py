from fastapi import FastAPI
from app.api.v1.endpoints import orders, stock

app = FastAPI(title="Order API")

app.include_router(orders.router, prefix="/api/v1", tags=["orders"])

app.include_router(stock.router, prefix="/api/v1", tags=["stock"])