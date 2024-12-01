from fastapi import APIRouter
from app.api.services.stock_service import get_stock
from app.api.models.stock import Stock

router = APIRouter()

@router.get("/stock", response_model=Stock)
def get_stock_endpoint():
    return get_stock()
