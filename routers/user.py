import time

from fastapi import APIRouter, Depends, Security

from models.user import User
from services.login.auth import authorized

router = APIRouter(prefix="/user", tags=["User"])


@router.get(
    "/{user_id}", dependencies=[Security(authorized, scopes=["MASTER", "MANAGER"])]
)
async def get_user_by_id(user_id: int) -> User:
    return await User.get(id=user_id)
