from datetime import datetime
from decimal import Decimal

from tortoise import ForeignKeyFieldInstance, Model, fields

from models.common import TimeStampMixin
from services.enums.currency import Currency
from services.enums.order_status import OrderStatus


class UserOrder(Model, TimeStampMixin):
    order_id: int = fields.BigIntField(pk=True)
    user: ForeignKeyFieldInstance = fields.ForeignKeyField(
        "models.User", related_name="user", db_constraint=False
    )
    status: OrderStatus = fields.CharEnumField(max_length=2, enum_type=OrderStatus)
    order_date: datetime = fields.DatetimeField(index=True)
    complete_date: datetime = fields.DatetimeField(null=True)
    from_cur: Currency = fields.CharEnumField(max_length=4, enum_type=Currency)
    to_cur: Currency = fields.CharEnumField(max_length=4, enum_type=Currency)
    from_amount: Decimal = fields.DecimalField(max_digits=12, decimal_places=3, default=0)
    to_amount: Decimal = fields.DecimalField(max_digits=12, decimal_places=3, default=0)
    user_account: ForeignKeyFieldInstance = fields.ForeignKeyField(
        "models.UserAccount",
        related_name="user_account",
        db_constraint=False,
        null=True,
    )
    usd_amount: Decimal = fields.DecimalField(
        max_digits=10, decimal_places=3, default=0
    )
    exchange_rate_id: str = fields.CharField(
        max_length=50, default=""
    )
    standard_rate: Decimal = fields.DecimalField(
        max_digits=10, decimal_places=3, default=0
    )
    saving_amount: Decimal = fields.DecimalField(
        max_digits=10, decimal_places=3, default=0
    )

    class Meta:
        ordering = ["-order_id"]
