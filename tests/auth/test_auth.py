import http
from datetime import datetime, timedelta

import pytest
from fastapi.security import SecurityScopes
from freezegun import freeze_time
from jose import jwt

from config.settings import settings
from services.exceptions.custom_execptions import (
    ForbiddenException,
    UnauthorizedException,
)
from services.login.auth import (
    MSG_ADMIN_ROLE_NOT_ENOUGH,
    MSG_INVALID_TOKEN,
    MSG_TOKEN_EXPIRE_NOT_FOUND,
    MSG_TOKEN_EXPIRED,
    MSG_USER_ID_NOT_FOUND,
    MSG_USER_ROLE_NOT_FOUND,
    SIGN_ALGORITHM,
    authorized,
)


class TestAuth:
    async def test_authorized_without_token(self):
        # Given: No token and scope
        scopes = SecurityScopes()

        # When: Try to check authorize
        # Then: HTTPException(HTTP_401_UNAUTHORIZED) raise with invalid token detail
        with pytest.raises(UnauthorizedException) as e:
            await authorized(security_scopes=scopes, token="")
        assert e.value.status_code == http.HTTPStatus.UNAUTHORIZED
        assert e.value.detail == MSG_INVALID_TOKEN

    async def test_authorized_without_user_id(self):
        # Given: Token without user_id
        scopes = SecurityScopes()
        data = {"role": "USER", "expire": datetime.now().timestamp()}
        token = jwt.encode(data, settings.TOKEN_KEY, algorithm=SIGN_ALGORITHM)

        # When: Try to check authorize
        # Then: HTTPException(HTTP_401_UNAUTHORIZED) raise with user id not found detail
        with pytest.raises(UnauthorizedException) as e:
            await authorized(security_scopes=scopes, token=token)
        assert e.value.status_code == http.HTTPStatus.UNAUTHORIZED
        assert e.value.detail == MSG_USER_ID_NOT_FOUND

    async def test_authorized_without_expire(self):
        # Given: Token without "expire" key
        scopes = SecurityScopes()
        data = {"user_id": "test", "role": "USER"}
        token = jwt.encode(data, settings.TOKEN_KEY, algorithm=SIGN_ALGORITHM)

        # When: Try to check authorize
        # Then: HTTPException(HTTP_401_UNAUTHORIZED) raise with expire not found detail
        with pytest.raises(UnauthorizedException) as e:
            await authorized(security_scopes=scopes, token=token)
        assert e.value.status_code == http.HTTPStatus.UNAUTHORIZED
        assert e.value.detail == MSG_TOKEN_EXPIRE_NOT_FOUND

    async def test_authorized_with_expired_token(self, get_token):
        # Given: Expired token
        scopes = SecurityScopes()
        with freeze_time("2022-10-16 23:59:59"):
            token = get_token()

        # When: Try to check authorize after expired time
        # Then: HTTPException(HTTP_401_UNAUTHORIZED) raise with token expired detail
        with freeze_time("2022-10-18"), pytest.raises(UnauthorizedException) as e:
            await authorized(security_scopes=scopes, token=token)
        assert e.value.status_code == http.HTTPStatus.UNAUTHORIZED
        assert e.value.detail == MSG_TOKEN_EXPIRED

    async def test_authorized_without_role(self):
        # Given: Token without role
        scopes = SecurityScopes()
        data = {
            "user_id": "test",
            "expire": (datetime.now() + timedelta(days=1)).timestamp(),
        }
        token = jwt.encode(data, settings.TOKEN_KEY, algorithm=SIGN_ALGORITHM)

        # When: Try to check authorize
        # Then: HTTPException(HTTP_401_UNAUTHORIZED) raise with role not found detail
        with pytest.raises(UnauthorizedException) as e:
            await authorized(security_scopes=scopes, token=token)
        assert e.value.status_code == http.HTTPStatus.UNAUTHORIZED
        assert e.value.detail == MSG_USER_ROLE_NOT_FOUND

    async def test_authorized_with_not_enough_scope(self, get_token):
        # Given: USER role token
        token = get_token()

        # When: Try to check authorize with MASTER scope
        scopes = SecurityScopes(["MASTER"])
        # Then: HTTPException(HTTP_401_UNAUTHORIZED) raise with not enough role detail
        with pytest.raises(ForbiddenException) as e:
            await authorized(security_scopes=scopes, token=token)
        assert e.value.status_code == http.HTTPStatus.FORBIDDEN
        assert e.value.detail == MSG_ADMIN_ROLE_NOT_ENOUGH
