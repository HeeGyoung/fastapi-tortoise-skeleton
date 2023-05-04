from datetime import datetime

from pydantic import BaseModel

from services.enums.order_status import OrderStatus


class OrderListResponse(BaseModel):
    id: int
    order_date: datetime
    status: OrderStatus
    user_id: int
    username: str
    amount: float
    complete_date: datetime
