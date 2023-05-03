from pydantic import BaseModel


class AdminUserResponse(BaseModel):
    username: str
    role: str

    class Config:
        orm_mode = True
