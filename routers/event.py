from fastapi import APIRouter

from models.event import Event
from schemas.request.event_request import EventRequest
from schemas.response.event_response import EventResponse

router = APIRouter(prefix="/event", tags=["Event"])


@router.post("", response_model=EventResponse)
async def create_event(event: EventRequest):
    return EventResponse.from_orm(await Event.create(**event.dict()))


@router.get("/{event_id}", response_model=EventResponse)
async def get_event(event_id: int):
    return EventResponse.from_orm(await Event.get(id=event_id))
