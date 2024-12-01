order_data = {
    1: {
        "created": "2024-09-10 12:00:00",
        "paid": False,
        "subtotal": 1050,
        "taxes": 5.5,
        "discounts": 0,
        "total": 1055.5,
        "user_id": 1,
        "user_name": "Paco Mendez",
        "items":[
            {"name": "Corona", "quantity": 2},
            {"name": "Club Colombia", "quantity": 2},
            {"name": "Quilmes", "quantity": 5},
        ],
        "rounds": [
            {
                "created": "2024-09-10 12:00:30",
                "items": [
                    {"name": "Corona", "quantity": 2},
                    {"name": "Club Colombia", "quantity": 1},
                ],
            },
            {
                "created": "2024-09-10 12:20:31",
                "items": [
                    {"name": "Club Colombia", "quantity": 1},
                    {"name": "Quilmes", "quantity": 2},
                ],
            },
            {
                "created": "2024-09-10 12:43:21",
                "items": [{"name": "Quilmes", "quantity": 3}],
            },
        ],
    },
    2: {
        "created": "2024-09-11 14:20:00",
        "paid": True,
        "subtotal": 2110,
        "taxes": 5.5,
        "total": 2115.5,
        "user_id": 2,
        "user_name": "Luis Morales",
        "discounts": 2,
        "items":[
            {"name": "Corona", "quantity": 14},
            {"name": "Club Colombia", "quantity": 5},
        ],
        "rounds": [
            {
                "created": "2024-09-11 14:20:30",
                "items": [
                    {"name": "Corona", "quantity": 2,},
                    {"name": "Club Colombia", "quantity": 1},
                ],
            },
            {
                "created": "2024-09-11 14:10:30",
                "items": [
                    {"name": "Corona", "quantity": 12},
                    {"name": "Club Colombia", "quantity": 4},
                ],
            },
        ],
    },
    3: {
        "created": "2024-09-11 14:20:00",
        "paid": True,
        "subtotal": 2110,
        "taxes": 5.5,
        "total": 2115.5,
        "user_id": 2,
        "user_name": "Marco Morales",
        "discounts": 2,
        "items":[
            {"name": "Corona", "quantity": 14},
            {"name": "Club Colombia", "quantity": 5},
        ],
        "rounds": [
            {
                "created": "2024-09-11 14:20:30",
                "items": [
                    {"name": "Corona", "quantity": 2,},
                    {"name": "Club Colombia", "quantity": 1},
                ],
            },
            {
                "created": "2024-09-11 14:10:30",
                "items": [
                    {"name": "Corona", "quantity": 12},
                    {"name": "Club Colombia", "quantity": 4},
                ],
            },
        ],
    },
}
