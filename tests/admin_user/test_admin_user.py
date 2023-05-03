import http

import pytest
from httpx import AsyncClient

from models.admin_user import AdminUser
from schemas.request.admin_user_request import AdminUserRequest
from services.admin_user import create_admin
from services.login.auth import MSG_ADMIN_ROLE_NOT_ENOUGH, crypt_context
from tests.utils.decorator import set_db


@pytest.mark.anyio
class TestAdminUser:
    def _get_admin_user_request(
        self, username: str = "test", password: str = "test", role: str = "USER"
    ):
        return AdminUserRequest(username=username, password=password, role=role)

    async def test_admin_user_request_form_should_password_hash(self):
        # Given: Set AdminUserRequest form with test password
        test_password = "test_password"

        # When: Password transformed through AdminUserRequest form
        admin_request = self._get_admin_user_request(password=test_password)

        # Then: password hashed
        assert admin_request.password != test_password
        assert crypt_context.verify(test_password, admin_request.password)

    async def test_create_admin_user_data(self):
        # Given: Set AdminUserRequest form
        admin_request = self._get_admin_user_request()

        # When: Create AdminUser data
        created_user = await create_admin(admin_request)

        # Then: AdminUser created and hashed password stored
        assert created_user.password == admin_request.password
        assert created_user.role == admin_request.role
        assert await AdminUser.exists(
            username=admin_request.username,
            password=admin_request.password,
            role=admin_request.role,
        )

    async def test_create_admin_user_api_without_token(self, client: AsyncClient):
        # Given: Test admin user
        admin_request = self._get_admin_user_request()

        # When: Try to create admin user
        response = await client.post("/admin", json=admin_request.dict())

        # Then: 401 UNAUTHORIZED returned
        assert response.status_code == http.HTTPStatus.UNAUTHORIZED

    async def test_create_admin_user_api_with_user_role_token(
        self, client: AsyncClient, get_token
    ):
        # Given: Test admin user and USER role token
        admin_request = self._get_admin_user_request()
        user_token = get_token()

        # When: Try to create admin user
        response = await client.post(
            "/admin",
            json=admin_request.dict(),
            headers={"Authorization": f"Bearer {user_token}"},
        )

        # Then: 403 FORBIDDEN returned and not enough role
        assert response.status_code == http.HTTPStatus.FORBIDDEN
        assert response.json()["detail"] == MSG_ADMIN_ROLE_NOT_ENOUGH

    async def test_create_admin_user(self, client: AsyncClient, get_token):
        # Given: Test admin user with MASTER role token
        new_admin_user = self._get_admin_user_request()
        master_token = get_token(role="MASTER")

        # When: Try to create admin user
        response = await client.post(
            "/admin",
            json=new_admin_user.dict(),
            headers={
                "Authorization": f"Bearer {master_token}",
                "accept": "application/json",
            },
        )

        # Then: 200 OK and admin user created
        assert response.status_code == http.HTTPStatus.OK
        assert await AdminUser.exists(username=new_admin_user.username)
