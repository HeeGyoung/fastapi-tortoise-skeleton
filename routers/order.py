from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate

from schemas.request.order_list_request import OrderListRequest
from schemas.response.order_list_response import OrderListResponse
from services.order import get_order_list

router = APIRouter(prefix="/order", tags=["Order"])


@router.get("/list", response_model=Page[OrderListResponse])
async def get_orders(form_data: OrderListRequest = Depends()):
    return paginate(await get_order_list(form_data))
