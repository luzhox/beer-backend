import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

@pytest.fixture
def fake_orders():
    return {
        1: {
            "created": datetime(2024, 9, 10, 12, 0, 0).isoformat(),
            "paid": False,
            "subtotal": 0,
            "taxes": 0,
            "discounts": 0,
            "user_id": 1,
            "user_name": "Paco Mendez",
             "rounds": [
                {
                    "created": datetime(2024, 9, 10, 12, 0, 30).isoformat(),
                    "items": [
                        {"name": "Corona", "quantity": 2},
                        {"name": "Club Colombia", "quantity": 1},
                    ],
                },
                {
                    "created": datetime(2024, 9, 10, 12, 20, 31).isoformat(),
                    "items": [
                        {"name": "Club Colombia", "quantity": 1},
                        {"name": "Quilmes", "price": 2},
                    ],
                },
                {
                    "created": datetime(2024, 9, 10, 12, 43, 21).isoformat(),
                    "items": [{"name": "Quilmes", "quantity": 3}],
                },
            ],
        },
        2: {
            "created": datetime(2024, 9, 11, 14, 20, 0).isoformat(),
            "paid": True,
            "subtotal": 30.5,
            "taxes": 5.5,
            "discounts": 2,
            "user_id": 1,
            "user_name": "Paco Mendez",
            "rounds": [],
        },
    }

def test_get_all_orders(fake_orders):
    response = client.get("/api/v1/orders")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    data = response.json()
    assert len(data) == len(fake_orders), f"Expected {len(fake_orders)} orders but got {len(data)}"

    for expected_order, actual_order in zip(fake_orders.values(), data):

        assert actual_order["created"] == expected_order["created"], f"Expected {expected_order['created']} but got {actual_order['created']}"
        assert expected_order["paid"] == actual_order["paid"], "Paid status mismatch"
        assert expected_order["subtotal"] == actual_order["subtotal"], "Subtotal mismatch"
        assert expected_order["taxes"] == actual_order["taxes"], "Taxes mismatch"
        assert expected_order["discounts"] == actual_order["discounts"], "Discounts mismatch"
        assert expected_order["items"] == actual_order["items"], "Items mismatch"
        assert expected_order["rounds"] == actual_order["rounds"], "Rounds mismatch"

def test_get_order_by_id_success(fake_orders):
    order_id = 1
    response = client.get(f"/api/v1/orders/{order_id}")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    data = response.json()
    expected_order = fake_orders[order_id]

    assert data["created"] == expected_order["created"], f"Expected {expected_order['created']} but got {data['created']}"
    assert data["paid"] == expected_order["paid"], "Paid status mismatch"
    assert data["subtotal"] == expected_order["subtotal"], "Subtotal mismatch"
    assert data["taxes"] == expected_order["taxes"], "Taxes mismatch"
    assert data["discounts"] == expected_order["discounts"], "Discounts mismatch"
    assert data["items"] == expected_order["items"], "Items mismatch"
    assert data["rounds"] == expected_order["rounds"], "Rounds mismatch"

def test_get_order_by_id_not_found():

    response = client.get("/api/v1/orders/999")
    assert response.status_code == 404, "Expected 404 for non-existent order"
    assert response.json() == {"detail": "Order not found"}
