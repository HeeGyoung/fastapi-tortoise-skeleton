from enum import Enum, auto

from services.enums import UpperStrEnum


class AccountType(UpperStrEnum):
    DOM = auto()
    FOR = auto()


class AccountStatus(str, Enum):
    ABLE = "1"
    UNABLE = "11"


class AccountAuthenticated(UpperStrEnum):
    NOT_YET = auto()
    SUCCESS = auto()
    FAIL = auto()
    PROCESSING = auto()
