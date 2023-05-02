from tortoise import Model, fields

from models.common import TimeStampMixin


class AdminUser(Model, TimeStampMixin):
    id: str = fields.CharField(pk=True, max_length=50)
    password: str = fields.CharField(max_length=64, null=True)
    role: str = fields.CharField(max_length=64, null=True)
