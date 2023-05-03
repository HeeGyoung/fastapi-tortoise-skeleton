from models.admin_user import AdminUser
from schemas.request.admin_user_request import AdminUserRequest


async def create_admin(user: AdminUserRequest):
    return await AdminUser.create(**user.dict())