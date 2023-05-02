import pytest

from models.order_manager import OrderManager
from models.user import User
from models.user_account import UserAccount
from models.user_order import UserOrder


@pytest.fixture
async def create_order_data_with_relations():
    async def _create_data(user: dict, account: dict, order: dict, manager: dict):
        created_user = await User.create(**user)
        created_account = await UserAccount.create(
            user_id=created_user.user_id, **account
        )
        created_order = await UserOrder.create(
            user=created_user, user_account=created_account, **order
        )
        created_manager = await OrderManager.create(
            order_id=created_order.order_id, **manager
        )
        return created_user, created_account, created_order, created_manager

    return _create_data
