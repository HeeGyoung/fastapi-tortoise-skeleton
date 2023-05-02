from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EventResponse(BaseModel):
    id: int
    start_date: datetime
    end_date: datetime
    title: str
    is_display: bool
    page_url: Optional[str] = None
    end_page_url: Optional[str] = None
    banner_image_url: Optional[str] = None
    list_image_url: Optional[str] = None
    is_delete: bool

    class Config:
        orm_mode = True
