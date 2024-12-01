# app/api/services/stock_service.py

from app.api.models.stock import Stock
from app.api.db.dummy_stock_data import stock_data

def get_stock() -> Stock:
    """
    Recupera el estado del stock actual.
    """
    return Stock(**stock_data)
