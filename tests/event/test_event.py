import http
from typing import Any, Dict, Optional

import pytest
from httpx import AsyncClient

from models.event import Event
from tests.utils.decorator import set_db


@pytest.mark.anyio
@set_db("exchange")
class TestEvent:
    async def test_create_event(self, client: AsyncClient):
        # Given: Event data
        data: Optional[Dict[Any, Any]] = {
            "start_date": "2022-10-04 00:00:00",
            "end_date": "2022-10-05 23:59:59",
            "title": "test event",
            "is_display": True,
            "page_url": "https://test.com",
            "end_page_url": "https://test.com",
            "banner_image_url": "https://test.com",
            "list_image_url": "https://test.com",
            "is_delete": False,
        }
        # When: Try to create new event
        response = await client.post(
            "/event",
            json=data,
        )
        # Then: response status is 200, the data is created and the transaction
        # will rollback.
        assert response.status_code == http.HTTPStatus.OK
        assert await Event.filter(id=response.json()["id"]).count() == 1

    async def test_rollback_executed(self, client: AsyncClient):
        # Given: transaction rollback from test_create_event function
        # When: Try to get rollback data
        response = await client.get("/event/1")
        # Then: http response is 200 but nothing returned.
        assert response.status_code == http.HTTPStatus.NOT_FOUND
