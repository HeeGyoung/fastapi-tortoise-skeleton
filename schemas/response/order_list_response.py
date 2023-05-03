from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, validator

from config.settings import settings
from services.crypto.cipher import decrypt_aes_cbc
from services.enums.order_status import OrderStatus
from services.enums.user import AccountLevel
from services.validator.helper import is_phone


class OrderListResponse(BaseModel):
    id: int
    order_date: datetime
    status: OrderStatus
    user_id: str
    user_name: str
    amount: float
    complete_date: datetime

