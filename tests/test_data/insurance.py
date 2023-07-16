parametrize_tariff_post = [
    (
        {
            "2021-01-01": [
                {"cargo": "Glass", "rate": 0.4},
                {"cargo": "Other", "rate": 0.2},
            ],
            "2021-01-03": [
                {"cargo": "Glass", "rate": 0.2},
                {"cargo": "Other", "rate": 0.5},
            ],
        },
        {"status": 200},
    ),
    (
        {"2021-01-aa": [{"cargo": "Glass", "rate": 0.4}]},
        {"status": 422, "msg": "invalid date format"},
    ),
    (
        {"2021-01-01": [{"cargo": "Glass", "rate": "a"}]},
        {"status": 422, "msg": "value is not a valid float"},
    ),
]

parametrize_calculate_price_get = [
    (
        {"cargo": "Glass", "date": "2021-01-01", "declared_value": 1000},
        {
            "status": 200,
            "body": {"actual_date": "2021-01-01", "cargo": "Glass", "price": 400.0},
        },
    ),
    (
        {"cargo": "Glass", "date": "2021-01-a", "declared_value": 1000},
        {"status": 422, "msg": "invalid date format"},
    ),
]

parametrize_insurance_get = [
    (
        {"page_number": 1, "page_size": 1},
        {"status": 200, "count": 1},
    ),
    (
        {"page_number": 1, "page_size": 2},
        {"status": 200, "count": 2},
    ),
    (
        {"page_number": 10, "page_size": 2},
        {"status": 200, "count": 0},
    ),
    (
        {"page_number": "e", "page_size": 2},
        {"status": 422, "msg": "value is not a valid integer"},
    ),
]
