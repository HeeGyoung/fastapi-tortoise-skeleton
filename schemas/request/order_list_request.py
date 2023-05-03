from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from services.enums.order_status import OrderStatus


class OrderListRequest(BaseModel):
    start_date: datetime
    end_date: datetime
    order_status: Optional[OrderStatus] = None
    user_id: Optional[str] = None
    username: Optional[str] = None
    order_id: Optional[int] = None
