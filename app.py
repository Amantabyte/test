from fastapi import FastAPI
from pydantic import BaseModel

from services.metrics import profit_margin
from services.pricing import final_price
from services.orders import create_order

app = FastAPI(title="Demo Support Product")


class MetricsRequest(BaseModel):
    profit: float
    revenue: float


class PricingRequest(BaseModel):
    price: float
    discount_percent: float


class OrderRequest(BaseModel):
    product_id: str
    quantity: int


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/metrics/profit-margin")
def metrics_profit_margin(request: MetricsRequest) -> dict:
    result = profit_margin(request.profit, request.revenue)
    return {"profit_margin": result}


@app.post("/pricing/final-price")
def pricing_final_price(request: PricingRequest) -> dict:
    result = final_price(request.price, request.discount_percent)
    return {"final_price": result}


@app.post("/orders")
def orders_create(request: OrderRequest) -> dict:
    order = create_order(request.product_id, request.quantity)
    return order
