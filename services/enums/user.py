from enum import Enum, auto

from services.enums import UpperStrEnum


class AccountLevel(UpperStrEnum):
    BRONZE = auto()
    SILVER = auto()
    GOLD = auto()


class AccountStatus(Enum):
    ACTIVE = 1
    INACTIVE = 0


class AccountAuthenticated(UpperStrEnum):
    NOT_YET = auto()
    EMAIL = auto()
    SNS = auto()
    PHONE = auto()