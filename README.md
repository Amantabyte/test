# Demo Support Product

This repository is a small demo backend for support-agent remediation testing. It includes a FastAPI app with intentionally seeded bugs in core service functions, designed so that automated bug-fixing workflows can identify and fix them.

## Intentional seeded bugs

- `services/metrics.py`: `profit_margin` divides by `revenue` and raises `ZeroDivisionError` when revenue is `0`.
- `services/pricing.py`: `final_price` subtracts `discount_percent` directly from `price` instead of treating it as a percentage.
- `services/orders.py`: `create_order` accepts zero or negative `quantity` values.

## Test behavior

The test suite is intentionally designed to demonstrate these bugs:

- `tests/test_metrics.py` fails for revenue `0`.
- `tests/test_pricing.py` fails for `price=200`, `discount_percent=10`.
- `tests/test_orders.py` fails for negative quantity.

## Structure

- `app.py` - FastAPI application with health, metrics, pricing, and order endpoints.
- `services/metrics.py` - profit margin service.
- `services/pricing.py` - pricing service.
- `services/orders.py` - order creation service.
- `tests/` - pytest test cases demonstrating the seeded bugs.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
uvicorn app:app --reload
```

## API Examples

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Profit margin:

```bash
curl -X POST http://127.0.0.1:8000/metrics/profit-margin \
  -H "Content-Type: application/json" \
  -d '{"profit": 20.0, "revenue": 100.0}'
```

Final price:

```bash
curl -X POST http://127.0.0.1:8000/pricing/final-price \
  -H "Content-Type: application/json" \
  -d '{"price": 200.0, "discount_percent": 10.0}'
```

Create order:

```bash
curl -X POST http://127.0.0.1:8000/orders \
  -H "Content-Type: application/json" \
  -d '{"product_id": "prod-123", "quantity": 2}'
```
