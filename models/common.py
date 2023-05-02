from datetime import datetime

from tortoise import fields


class TimeStampMixin:
    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)
