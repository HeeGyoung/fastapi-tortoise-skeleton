from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from services.enums.currency import Currency
from services.enums.order_status import OrderStatus


class OrderListRequest(BaseModel):
    start_date: datetime
    end_date: datetime
    order_status: Optional[OrderStatus] = None
    currency: Optional[Currency] = None
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    user_eng_name: Optional[str] = None
    order_id: Optional[int] = None
