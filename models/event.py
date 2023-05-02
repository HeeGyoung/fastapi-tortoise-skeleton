from datetime import datetime

from tortoise import Model, fields
from tortoise.fields import BooleanField

from models.common import TimeStampMixin


class Event(Model, TimeStampMixin):
    id: int = fields.BigIntField(pk=True)
    start_date: datetime = fields.DatetimeField()
    end_date: datetime = fields.DatetimeField()
    title: str = fields.CharField(max_length=50)
    is_display: BooleanField = fields.BooleanField()
    page_url: str = fields.CharField( max_length=2048, null=True)
    end_page_url: str = fields.CharField(
        max_length=2048, null=True
    )
    banner_image_url: str = fields.CharField(
        max_length=2048, null=True
    )
    list_image_url: str = fields.CharField(
        max_length=2048, null=True
    )
    is_delete: BooleanField = fields.BooleanField(
        default=True, null=True
    )
