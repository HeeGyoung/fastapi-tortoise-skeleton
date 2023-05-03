from enum import auto

from services.enums import UpperStrEnum


class OrderStatus(UpperStrEnum):
    REQUEST = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    CANCEL_AUTO = auto()
    CANCEL_USER = auto()
    CANCEL_ADMIN = auto()
