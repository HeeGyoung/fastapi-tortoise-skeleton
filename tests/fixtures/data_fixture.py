import pytest

from models.user import User
from models.user_order import UserOrder


@pytest.fixture
async def create_order_data_with_relations():
    async def _create_data(user: dict, account: dict, order: dict, manager: dict):
        created_user = await User.create(**user)
        created_account = await User.create(
            user_id=created_user.user_id, **account
        )
        created_order = await UserOrder.create(
            user=created_user, user_account=created_account, **order
        )
        return created_user, created_account, created_order

    return _create_data
