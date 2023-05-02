from pydantic import BaseModel, validator

from services.login.auth import get_hashed_password


class AdminUserRequest(BaseModel):
    id: str
    password: str
    role: str

    @validator("password")
    def hash_password(cls, v):
        return get_hashed_password(v)
