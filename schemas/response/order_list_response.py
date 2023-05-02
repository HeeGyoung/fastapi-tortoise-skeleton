from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, validator

from config.settings import settings
from services.crypto.cipher import decrypt_aes_cbc
from services.enums.currency import Currency
from services.enums.order_status import OrderStatus
from services.enums.user_account import AccountType
from services.validator.helper import is_phone


class OrderListResponse(BaseModel):
    order_id: int
    order_date: datetime
    status: OrderStatus
    from_cur: Currency
    from_amount: Decimal
    to_cur: Currency
    to_amount: Decimal
    standard_rate: Decimal
    user_id: str
    user_name: str
    user_eng_name: Optional[str] = None
    user_mobile: str
    account_type: AccountType
    bank_code: str
    bank_name: str
    account_number: str
    account_holder: Optional[str]
    alias: Optional[str]
    deposit_time: Optional[datetime]
    withdraw_time: Optional[datetime]
    is_confirm: Optional[bool]
    comment: Optional[str]
    firm_id: Optional[int]

    @validator("user_mobile")
    def decode_user_mobile(cls, v):
        if not is_phone(v):
            return decrypt_aes_cbc(settings.AES_KEY, settings.AES_KEY, v)
        return v
