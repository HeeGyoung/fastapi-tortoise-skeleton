from tortoise import Model, fields
from tortoise.fields import BooleanField

from models.common import TimeStampMixin
from services.enums.user import AccountAuthenticated, AccountLevel, AccountStatus


class User(Model, TimeStampMixin):
    id: int = fields.BigIntField(pk=True)
    username: str = fields.CharField(max_length=10)
    password: str = fields.CharField(max_length=60)
    account_level: AccountLevel = fields.CharEnumField(enum_type=AccountLevel)
    status: AccountStatus = fields.BooleanField(
        enum_type=AccountStatus, default=AccountStatus.ACTIVE
    )
    authenticated: AccountAuthenticated = fields.CharEnumField(
        enum_type=AccountAuthenticated, default="NOT_YET"
    )
