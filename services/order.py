from typing import Any, Dict

from models.user_order import UserOrder
from schemas.request.order_list_request import OrderListRequest


def get_user_order_condition(form_data: OrderListRequest) -> Dict[str, Any]:
    kwargs: Dict[str, Any] = {
        "order_date__gte": form_data.start_date,
        "order_date__lte": form_data.end_date,
    }
    if form_data.order_status:
        kwargs["status"] = form_data.order_status
    if form_data.order_id:
        kwargs["id"] = form_data.order_id
    return kwargs


def get_user_condition(form_data: OrderListRequest) -> Dict[str, Any]:
    kwargs: Dict[str, Any] = {}
    if form_data.user_id:
        kwargs["user__id"] = form_data.user_id
    if form_data.username:
        kwargs["user__username"] = form_data.username
    return kwargs


async def get_order_list(form_data: OrderListRequest):
    orders = await UserOrder.filter(
        **get_user_condition(form_data),
        **get_user_order_condition(form_data),
    ).values(
        "id",
        "order_date",
        "status",
        "amount",
        "complete_date",
        user_id="user__id",
        username="user__username",
    )
    return orders
