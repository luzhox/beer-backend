from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Item(BaseModel):
    name: str
    quantity: Optional[int] = 1
    price: Optional[float] = 0

class Round(BaseModel):
    created: datetime
    items: List[Item]

class Order(BaseModel):
    created: datetime
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    total: float
    user_id: int
    user_name: str
    rounds: List[Round]
    items: List[Item]
