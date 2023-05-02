from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from services.exceptions.custom_execptions import UnauthorizedException
from services.login.auth import (
    MSG_NOT_AUTHORIZED,
    create_token,
    get_admin_user,
    verify_password,
)

router = APIRouter(prefix="/login")


@router.post("")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    admin_user = await get_admin_user(form_data.username)
    if not verify_password(form_data.password, admin_user.password):
        raise UnauthorizedException(MSG_NOT_AUTHORIZED)
    return create_token(admin_user)
