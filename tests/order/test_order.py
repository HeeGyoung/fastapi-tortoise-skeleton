import http

import pytest
from httpx import AsyncClient

from schemas.response.order_list_response import OrderListResponse
from services.enums.order_status import OrderStatus
from services.enums.user import AccountLevel, AccountAuthenticated
from services.login.auth import get_hashed_password
from tests.utils.decorator import set_db


@pytest.mark.anyio
@set_db("default")
class TestGetOrder:
    async def _create_simple_data(self, create_order_data_with_relations):
        return await create_order_data_with_relations(
            user={
                "username": "test_user",
                "password": get_hashed_password("password"),
                "account_level": AccountLevel.SILVER.value,
                "status": 1,
                "authenticated": AccountAuthenticated.SNS.value
            },
            order={
                "status": OrderStatus.REQUEST.value,
                "order_date": "2023-05-02 11:00:00",
                "complete_date": "2023-05-02 11:00:00",
                "amount": 1000000,
            },
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
                "start_date": "2023-05-03 00:00:00",
                "end_date": "2023-05-03 23:59:59",
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
        user, order = await self._create_simple_data(
            create_order_data_with_relations
        )

        # When: Try to get order list
        response = await self._call_order_list_api(
            {
                "start_date": "2023-05-02 00:00:00",
                "end_date": "2023-05-03 23:59:59",
            },
            client,
            get_token,
        )

        # Then: created data in the Given stage returned
        result = OrderListResponse(**response.json()["items"][0])
        assert response.status_code == http.HTTPStatus.OK
        assert len(response.json()["items"]) == 1
        assert result.id == order.id
        assert result.user_id == order.user.id
        assert result.username == order.user.username

    async def test_get_order_list_with_user_info(
        self, client: AsyncClient, get_token, create_order_data_with_relations
    ):
        # Given: create user, account, order, manager
        user, order = await self._create_simple_data(
            create_order_data_with_relations
        )

        # When: Try to get order list
        response = await self._call_order_list_api(
            {
                "start_date": "2023-05-02 00:00:00",
                "end_date": "2023-05-03 23:59:59",
                "user_id": user.id,
                "username": "test_user",
            },
            client,
            get_token,
        )

        # Then: created data in the Given stage returned
        result = OrderListResponse(**response.json()["items"][0])
        assert response.status_code == http.HTTPStatus.OK
        assert len(response.json()["items"]) == 1
        assert result.id == order.id
        assert result.user_id == order.user.id
        assert result.username == order.user.username
