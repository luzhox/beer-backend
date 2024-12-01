import pytest
from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)

@pytest.fixture
def stock_data():
    return {
        "last_updated": "2024-09-10 12:00:00",
        "beers": [
            {"name": "Corona", "price": 115, "quantity": 2},
            {"name": "Quilmes", "price": 120, "quantity": 0},
            {"name": "Club Colombia", "price": 110, "quantity": 3},
        ],
    }


def test_get_stock_success(stock_data):

    response = client.get("/api/v1/stock")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    
    data = response.json()
    assert data["last_updated"] == stock_data["last_updated"], "Last updated mismatch"
    assert len(data["beers"]) == len(stock_data["beers"]), "Beer list length mismatch"
    
    for expected_beer, actual_beer in zip(stock_data["beers"], data["beers"]):
        assert expected_beer["name"] == actual_beer["name"], f"Expected {expected_beer['name']} but got {actual_beer['name']}"
        assert expected_beer["price"] == actual_beer["price"], f"Expected {expected_beer['price']} but got {actual_beer['price']}"
        assert expected_beer["quantity"] == actual_beer["quantity"], f"Expected {expected_beer['quantity']} but got {actual_beer['quantity']}"
