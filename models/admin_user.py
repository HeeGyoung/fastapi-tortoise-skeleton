from tortoise import Model, fields

from models.common import TimeStampMixin


class AdminUser(Model, TimeStampMixin):
    id: int = fields.IntField(pk=True)
    username: str = fields.CharField(max_length=10)
    password: str = fields.CharField(max_length=60)
    role: str = fields.CharField(max_length=10)
