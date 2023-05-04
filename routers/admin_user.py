from fastapi import APIRouter, Security

from schemas.request.admin_user_request import AdminUserRequest
from schemas.response.admin_user_response import AdminUserResponse
from services.admin_user import create_admin
from services.login.auth import authorized

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.post(
    "",
    response_model=AdminUserResponse,
    dependencies=[Security(authorized, scopes=["MASTER"])],
)
async def create_admin_user(admin: AdminUserRequest):
    return AdminUserResponse.from_orm(await create_admin(admin))
