import http

import pytest
from httpx import AsyncClient

from schemas.response.order_list_response import OrderListResponse
from services.enums.order_status import OrderStatus
from tests.utils.decorator import set_db


@pytest.mark.anyio
@set_db("exchange")
@set_db("admin")
class TestGetOrder:
    async def _create_simple_data(self, create_order_data_with_relations):
        return await create_order_data_with_relations(
            user={
                "user_id": "test_user",
                "user_name": "test_user",
                "user_eng_name": "test_user",
                "user_mobile": "01012341234",
            },
            account={
                "account_type": "DOM",
                "account_number": "12341234",
            },
            order={
                "status": OrderStatus.REQUEST.value,
                "order_date": "2022-11-01 11:00:00",
                "from_amount": 1000000,
                "to_amount": 1000000,
            },
            manager={"deposit_time": "2022-11-01 11:30:00"},
        )

    async def _call_order_list_api(self, params: dict, client: AsyncClient, get_token):
        master_token = get_token(role="MASTER")
        return await client.get(
            "/order/list",
            params=params,
            headers={
                "Authorization": f"Bearer {master_token}",
                "accept": "application/json",
            },
        )

    async def test_get_order_list_out_of_datetime_range(
        self, client: AsyncClient, get_token, create_order_data_with_relations
    ):
        # Given: create user, account, order, manager
        await self._create_simple_data(create_order_data_with_relations)

        # When: Try to get order list
        response = await self._call_order_list_api(
            {
                "start_date": "2022-11-11 00:00:00",
                "end_date": "2022-11-11 23:59:59",
            },
            client,
            get_token,
        )

        # Then: empty list returned
        assert response.status_code == http.HTTPStatus.OK
        assert response.json()["items"] == []

    async def test_get_order_list_with_order_date(
        self, client: AsyncClient, get_token, create_order_data_with_relations
    ):
        # Given: create user, account, order, manager
        user, account, order, manager = await self._create_simple_data(
            create_order_data_with_relations
        )

        # When: Try to get order list
        response = await self._call_order_list_api(
            {
                "start_date": "2022-11-01 00:00:00",
                "end_date": "2022-11-01 23:59:59",
            },
            client,
            get_token,
        )

        # Then: created data in the Given stage returned
        result = OrderListResponse(**response.json()["items"][0])
        assert response.status_code == http.HTTPStatus.OK
        assert len(response.json()["items"]) == 1
        assert result.order_id == order.order_id
        assert result.user_id == order.user.user_id
        assert result.user_name == order.user.user_name
        assert result.user_eng_name == order.user.user_eng_name
        assert result.account_number == account.account_number
        assert result.deposit_time == manager.deposit_time

    async def test_get_order_list_with_user_info(
        self, client: AsyncClient, get_token, create_order_data_with_relations
    ):
        # Given: create user, account, order, manager
        user, account, order, manager = await self._create_simple_data(
            create_order_data_with_relations
        )

        # When: Try to get order list
        response = await self._call_order_list_api(
            {
                "start_date": "2022-11-01 00:00:00",
                "end_date": "2022-11-01 23:59:59",
                "user_id": "test_user",
                "user_name": "test_user",
                "user_eng_name": "test_user",
            },
            client,
            get_token,
        )

        # Then: created data in the Given stage returned
        result = OrderListResponse(**response.json()["items"][0])
        assert response.status_code == http.HTTPStatus.OK
        assert len(response.json()["items"]) == 1
        assert result.order_id == order.order_id
        assert result.user_id == order.user.user_id
        assert result.user_name == order.user.user_name
        assert result.user_eng_name == order.user.user_eng_name
        assert result.account_number == account.account_number
        assert result.deposit_time == manager.deposit_time
