from datetime import datetime, timezone
import uuid


def create_order(product_id: str, quantity: int) -> dict:
    order_id = str(uuid.uuid4())
    created_at = datetime.now(timezone.utc).isoformat()
    return {
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity,
        "status": "created",
        "created_at": created_at,
    }
