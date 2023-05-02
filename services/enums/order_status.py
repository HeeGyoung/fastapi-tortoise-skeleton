from enum import Enum


class OrderStatus(str, Enum):
    REQUEST = "10"
    PROCESSING = "20"
    PROCESSING_DEPOSIT_FIRMBANKING = "21"
    PROCESSING_WITHDRAW_FIRMBANKING = "25"
    PROCESSING_OPS_REQUIRED = "29"
    COMPLETED = "30"
    CANCEL_USER = "91"
    CANCEL_ADMIN = "92"
    CANCEL_OPENBANKING = "93"
    CANCEL_OVER_TIME = "94"
    CANCEL = "99"
