from services.pricing import final_price


def test_final_price_normal_case() -> None:
    assert final_price(100.0, 10.0) == 90.0


def test_final_price_percentage_bug() -> None:
    assert final_price(200.0, 10.0) == 180.0
