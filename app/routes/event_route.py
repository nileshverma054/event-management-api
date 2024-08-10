from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT

from app.schemas.event_schema import (
    EventCreateRequestSchema,
    EventSchema,
    EventUpdateRequestSchema,
    RegisterEventResponseSchema,
)
from app.services import event_service
from app.models.user_model import UserModel
from app.utils.auth_utils import authenticate_user, authenticate_and_authorize_user
from app.utils.database import get_db
from app.utils.logger import logger

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("", response_model=EventSchema)
async def create_event(
    event: EventCreateRequestSchema,
    current_user: UserModel = Depends(authenticate_and_authorize_user(permission="create_event")),
    db: Session = Depends(get_db),
):
    return event_service.create_event(db=db, event=event)


@router.get("", response_model=list[EventSchema])
async def get_events(
    title: str = Query(None),
    date: str = Query(None),
    location: str = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    events = event_service.get_events(
        db=db, title=title, date=date, location=location, skip=skip, limit=limit
    )
    return events


@router.get("/{event_id}", response_model=EventSchema)
async def get_event(event_id: int, db: Session = Depends(get_db)):
    db_event = event_service.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


@router.put("/{event_id}", response_model=EventSchema)
async def update_event(
    event_id: int,
    event: EventUpdateRequestSchema,
    db: Session = Depends(get_db),
    current_user: dict = Depends(authenticate_and_authorize_user),
):
    return event_service.update_event(db=db, event_id=event_id, event=event)


@router.delete("/{event_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_event(
    event_id: int,
    current_user: dict = Depends(authenticate_user),
    db: Session = Depends(get_db),
):
    return {}
    event_service.delete_event(db=db, event_id=event_id)


@router.post("/{event_id}/register", response_model=RegisterEventResponseSchema)
async def register_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(authenticate_user),
):
    logger.debug(f"event_id: {event_id}")
    return event_service.register_event(
        db=db, event_id=event_id, user_id=current_user.get("user_id")
    )
