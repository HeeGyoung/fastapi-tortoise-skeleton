from typing import AsyncIterator

from httpx import AsyncClient
from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError, OperationalError

from config.settings import TORTOISE_ORM
from main import app
from models.admin_user import AdminUser
from services.login.auth import create_token
from tests.fixtures.data_fixture import *  # noqa: F403


@pytest.fixture(scope="session", autouse=True)
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(app=app, base_url="http://tests") as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
async def initialize():
    await Tortoise.init(TORTOISE_ORM)
    try:
        await Tortoise._drop_databases()
    except (DBConnectionError, OperationalError):
        pass
    await Tortoise.init(TORTOISE_ORM, _create_db=True)
    await Tortoise.generate_schemas(safe=False)
    yield
    await Tortoise._drop_databases()


@pytest.fixture
def get_token():
    def _get_token(username: str = "test", password: str = "test", role: str = "USER"):
        admin_user = AdminUser(
            username=username,
            password=password,
            role=role,
        )
        token_response = create_token(admin_user)
        return token_response["access_token"]

    return _get_token
