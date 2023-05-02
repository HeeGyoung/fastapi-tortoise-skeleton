import time

from fastapi import APIRouter

from models.user_account import UserAccount

router = APIRouter(prefix="/user", tags=["UserAccount"])


@router.get("/{user_id}")
async def get_user(user_id: str) -> UserAccount:
    return await UserAccount.get(id=user_id)
