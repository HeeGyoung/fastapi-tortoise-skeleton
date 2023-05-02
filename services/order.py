from typing import Any, Dict

from models.user_order import UserOrder
from schemas.request.order_list_request import OrderListRequest


def get_user_order_condition(form_data: OrderListRequest):
    kwargs: Dict[str, Any] = {
        "order_date__gte": form_data.start_date,
        "order_date__lte": form_data.end_date,
    }
    if form_data.order_status:
        kwargs["status"] = form_data.order_status
    if form_data.currency:
        kwargs["from_cur"] = form_data.currency
    if form_data.order_id:
        kwargs["order_id"] = form_data.order_id
    return kwargs


def get_user_condition(form_data: OrderListRequest):
    kwargs = {}
    if form_data.user_id:
        kwargs["user__user_id"] = form_data.user_id
    if form_data.user_name:
        kwargs["user__user_name"] = form_data.user_name
    if form_data.user_eng_name:
        kwargs["user__user_eng_name"] = form_data.user_eng_name
    return kwargs


async def get_order_list(form_data: OrderListRequest):
    orders = await UserOrder.filter(
        **get_user_condition(form_data),
        **get_user_order_condition(form_data),
    ).values(
        "order_id",
        "order_date",
        "status",
        "from_cur",
        "from_amount",
        "to_cur",
        "to_amount",
        "standard_rate",
        user_id="user__user_id",
        user_name="user__user_name",
        user_eng_name="user__user_eng_name",
        user_mobile="user__user_mobile",
        account_type="user_account__account_type",
        bank_code="user_account__bank_code",
        bank_name="user_account__bank_name",
        account_number="user_account__account_number",
        account_holder="user_account__account_holder",
        alias="user_account__alias",
    )
    return orders
