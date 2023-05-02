import http
from datetime import datetime, timedelta

import pytest
from freezegun import freeze_time
from httpx import AsyncClient
from jose import jwt
from passlib.exc import UnknownHashError

from config.settings import settings
from models.admin_user import AdminUser
from services.login.auth import (
    ACCESS_TOKEN_EXPIRE_DAY,
    MSG_NOT_AUTHORIZED,
    SIGN_ALGORITHM,
    Token,
    crypt_context,
    get_hashed_password,
)
from tests.utils.decorator import set_db


@pytest.mark.anyio
@set_db("admin")
class TestLogin:
    async def _create_admin_user(
        self, id: str = "test", password: str = "test", role: str = "USER"
    ):
        return await AdminUser.create(id=id, password=password, role=role)

    async def test_login_with_not_exist_user(self, client: AsyncClient):
        # Given: Not create admin user
        # When: Try to login
        response = await client.post(
            "/login",
            data={"username": "not_exist_user_id", "password": "test_password"},
            headers={"accept": "application/json"},
        )
        # Then: AdminUser DoesNotExist return
        assert response.status_code == http.HTTPStatus.NOT_FOUND

    async def test_login_with_not_hashed_password(self, client: AsyncClient):
        # Given: AdminUser does not have hashed password
        admin_user = await self._create_admin_user()

        # When: Try to login
        # Then: Hash error occured
        with pytest.raises(UnknownHashError):
            await client.post(
                "/login",
                data={"username": admin_user.id, "password": admin_user.password},
                headers={"accept": "application/json"},
            )

    async def test_login_with_wrong_password(self, client: AsyncClient):
        # Given: Create admin user
        hashed_password = get_hashed_password("origin_password")
        admin_user = await self._create_admin_user(password=hashed_password)

        # When: Try to login with wrong password
        wrong_password = "forgot_password"
        response = await client.post(
            "/login",
            data={"username": admin_user.id, "password": wrong_password},
            headers={"accept": "application/json"},
        )

        # Then: Fail to verify password hash
        assert not crypt_context.verify(wrong_password, hashed_password)
        assert response.status_code == http.HTTPStatus.UNAUTHORIZED
        assert response.json()["detail"] == MSG_NOT_AUTHORIZED

    async def test_login(self, client: AsyncClient):
        # Given: Create admin user
        password = "test"
        admin_user = await self._create_admin_user(
            password=get_hashed_password(password)
        )

        with freeze_time("2022-10-18"):
            # When: Try to login
            response = await client.post(
                "/login",
                data={"username": admin_user.id, "password": password},
                headers={"accept": "application/json"},
            )

            token_data = Token(
                user_id=admin_user.id,
                role=admin_user.role,
                expire=(
                    datetime.now() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAY)
                ).timestamp(),
            ).dict()

        # Then: OK and token returned
        expected_token = jwt.encode(
            token_data, settings.TOKEN_KEY, algorithm=SIGN_ALGORITHM
        )
        assert response.status_code == http.HTTPStatus.OK
        assert response.json()["access_token"] == expected_token
