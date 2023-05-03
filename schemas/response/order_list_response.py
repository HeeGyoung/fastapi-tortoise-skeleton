from datetime import datetime

from pydantic import BaseModel

from services.enums.order_status import OrderStatus


class OrderListResponse(BaseModel):
    id: int
    order_date: datetime
    status: OrderStatus
    user_id: str
    user_name: str
    amount: float
    complete_date: datetime

