from tortoise import Model, fields
from tortoise.fields import BooleanField

from models.common import TimeStampMixin
from services.enums.user_account import AccountAuthenticated, AccountStatus, AccountType


class UserAccount(Model, TimeStampMixin):
    id: int = fields.BigIntField(pk=True)
    user_id: str = fields.CharField(max_length=10)
    account_type: AccountType = fields.CharEnumField(
        max_length=4, enum_type=AccountType
    )
    bank_code: str = fields.CharField(
        max_length=10, default="0"
    )
    bank_name: str = fields.CharField(
        max_length=50, default="0"
    )
    account_number: str = fields.CharField(max_length=50)
    account_holder: str = fields.CharField(
        max_length=50, null=True
    )
    alias: str = fields.CharField(
        max_length=50, null=True, default=""
    )
    is_primary: BooleanField = fields.BooleanField(
        default=False
    )
    status: AccountStatus = fields.CharEnumField(
        max_length=2, enum_type=AccountStatus, default="1"
    )
    authenticated: AccountAuthenticated = fields.CharEnumField(
        max_length=32, enum_type=AccountAuthenticated, default="NOT_YET"
    )
