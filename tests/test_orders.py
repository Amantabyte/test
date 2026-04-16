from services.orders import create_order


def test_create_order_valid_quantity() -> None:
    order = create_order("prod-123", 2)
    assert order["product_id"] == "prod-123"
    assert order["quantity"] == 2


def test_create_order_negative_quantity() -> None:
    order = create_order("prod-123", -1)
    assert order["quantity"] > 0
