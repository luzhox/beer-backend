from pydantic import BaseModel
from typing import List

class Beer(BaseModel):
    name: str
    price: float
    originalPrice: float
    quantity: int

class Stock(BaseModel):
    last_updated: str
    beers: List[Beer]
