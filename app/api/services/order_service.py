from datetime import datetime
from app.api.models.order import Order
from app.api.db.dummy_order_data import order_data

def get_order_by_id(order_id: int) -> Order:
    if order_id not in order_data:
        raise ValueError("Order not found")
    return Order(**order_data[order_id])

def get_all_orders() -> list[Order]:
    return [Order(**order_data) for order_data in order_data.values()]
