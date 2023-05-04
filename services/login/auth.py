from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from config.settings import settings
from models.admin_user import AdminUser
from schemas.response.token_response import TokenResponse
from services.exceptions.custom_execptions import (
    ForbiddenException,
    UnauthorizedException,
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login", scopes={"DEV": "dev", "MANAGER": "manager", "MASTER": "master"}
)

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ACCESS_TOKEN_EXPIRE_DAY = 1
ALGORITHM = "HS256"

MSG_NOT_AUTHORIZED = "Not authorized user"
MSG_USERNAME_NOT_FOUND = "Username not found"
MSG_TOKEN_EXPIRE_NOT_FOUND = "Expire not found"
MSG_TOKEN_EXPIRED = "Token expired"
MSG_USER_ROLE_NOT_FOUND = "Role not found"
MSG_ADMIN_ROLE_NOT_ENOUGH = "Not enough permission"
MSG_INVALID_TOKEN = "Invalid token"


class Token(BaseModel):
    username: str
    role: str
    expire: float


def get_hashed_password(password: str) -> str:
    return crypt_context.hash(password)


async def get_admin_user(username: str) -> AdminUser:
    return await AdminUser.get(username=username)


def verify_password(password: str, compare_password: str) -> bool:
    return crypt_context.verify(password, compare_password)


def create_token(user: AdminUser) -> dict:
    data = Token(
        username=user.username,
        role=user.role,
        expire=(datetime.now() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAY)).timestamp(),
    ).dict()
    return TokenResponse(
        access_token=jwt.encode(data, settings.TOKEN_KEY, algorithm=ALGORITHM),
        token_type="bearer",
    ).dict()


async def authorized(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
) -> Token:
    try:
        payload = jwt.decode(token, settings.TOKEN_KEY, algorithms=[ALGORITHM])
        user_id: Optional[str] = payload.get("username")
        if not user_id:
            raise UnauthorizedException(MSG_USERNAME_NOT_FOUND)
        token_expire: Optional[float] = payload.get("expire")
        if not token_expire:
            raise UnauthorizedException(MSG_TOKEN_EXPIRE_NOT_FOUND)
        if token_expire < datetime.now().timestamp():
            raise UnauthorizedException(MSG_TOKEN_EXPIRED)
        role: Optional[str] = payload.get("role")
        if not role:
            raise UnauthorizedException(MSG_USER_ROLE_NOT_FOUND)
        if security_scopes.scopes and role not in security_scopes.scopes:
            raise ForbiddenException(MSG_ADMIN_ROLE_NOT_ENOUGH)
    except JWTError:
        raise UnauthorizedException(MSG_INVALID_TOKEN)
    return Token(**payload)
