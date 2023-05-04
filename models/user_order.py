from datetime import datetime
from decimal import Decimal

from tortoise import ForeignKeyFieldInstance, Model, fields

from models.common import TimeStampMixin
from services.enums.order_status import OrderStatus


class UserOrder(Model, TimeStampMixin):
    id: int = fields.BigIntField(pk=True)
    user: ForeignKeyFieldInstance = fields.ForeignKeyField(
        "models.User", related_name="user", db_constraint=False
    )
    status: OrderStatus = fields.CharEnumField(max_length=20, enum_type=OrderStatus)
    order_date: datetime = fields.DatetimeField(index=True)
    complete_date: datetime = fields.DatetimeField(null=True)
    amount: Decimal = fields.DecimalField(max_digits=10, decimal_places=3, default=0)

    class Meta:
        ordering = ["-id"]
