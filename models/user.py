from tortoise import Model, fields
from tortoise.fields import BooleanField

from models.common import TimeStampMixin
from services.enums.user_status import UserStatus


class User(Model, TimeStampMixin):
    user_id: str = fields.CharField(pk=True, max_length=10)
    user_name: str = fields.CharField(max_length=50)
    user_eng_name: str = fields.CharField(
        null=True, max_length=50
    )
    user_mobile: str = fields.CharField(max_length=64)
    gender: str = fields.CharField(max_length=1, null=True, default="")
    birthdate: str = fields.CharField(max_length=8, null=True, default="")
    is_identity: BooleanField = fields.BooleanField(
        default=False
    )
    is_dom_account: BooleanField = fields.BooleanField(
        default=False, null=True
    )
    is_for_account: BooleanField = fields.BooleanField(
        default=False, null=True
    )
    is_email: BooleanField = fields.BooleanField(
        default=False, null=True
    )
    account_password: str = fields.CharField(
        max_length=64, null=True, default=""
    )
    lock_count: int = fields.IntField(default=0)
    user_status: UserStatus = fields.CharEnumField(
        max_length=2, enum_type=UserStatus, default="0"
    )
    comment: str = fields.CharField(max_length=300, null=True)
