from fastapi import APIRouter, HTTPException
from app.api.services.order_service import get_order_by_id, get_all_orders
from app.api.models.order import Order

router = APIRouter()

@router.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    try:
        return get_order_by_id(order_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/orders", response_model=list[Order])
def get_orders():
    try:
        return get_all_orders()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
# Compare this snippet from beer-tech/beer-backend/app/api/db/dummy_order_data.py: