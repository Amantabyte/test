import pytest
from services.metrics import profit_margin


def test_profit_margin_normal_case() -> None:
    assert profit_margin(20.0, 100.0) == 0.2


def test_profit_margin_zero_revenue() -> None:
    assert profit_margin(10.0, 0.0) == 0.0
