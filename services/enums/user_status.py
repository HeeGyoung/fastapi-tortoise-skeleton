from enum import Enum


class UserStatus(str, Enum):
    NORMAL = "0"
    ESCALATED = "91"
    WITHDRAWAL = "99"
