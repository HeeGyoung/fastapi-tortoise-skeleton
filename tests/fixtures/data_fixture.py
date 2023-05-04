import pytest

from models.user import User
from models.user_order import UserOrder


@pytest.fixture
async def create_order_data_with_relations():
    async def _create_data(user: dict, order: dict):
        created_user = await User.create(**user)
        created_order = await UserOrder.create(
            user=created_user, **order
        )
        return created_user, created_order

    return _create_data
