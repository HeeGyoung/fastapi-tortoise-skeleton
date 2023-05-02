from pydantic import BaseModel


class AdminUserResponse(BaseModel):
    id: str
    role: str

    class Config:
        orm_mode = True
