from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT

from app.schemas.event_schema import (
    EventCreateRequestSchema,
    EventSchema,
    EventUpdateRequestSchema,
)
from app.services import event_service
from app.utils.database import get_db
from app.utils.logger import logger

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("", response_model=EventSchema)
async def create_event(event: EventCreateRequestSchema, db: Session = Depends(get_db)):
    logger.debug(f"event: {event}")
    return event_service.create_event(db=db, event=event)


@router.get("", response_model=list[EventSchema])
async def get_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    events = event_service.get_events(db, skip=skip, limit=limit)
    return events


@router.get("/{event_id}", response_model=EventSchema)
async def get_event(event_id: int, db: Session = Depends(get_db)):
    db_event = event_service.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


@router.put("/{event_id}", response_model=EventSchema)
async def update_event(
    event_id: int, event: EventUpdateRequestSchema, db: Session = Depends(get_db)
):
    return event_service.update_event(db=db, event_id=event_id, event=event)


@router.delete("/{event_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_event(event_id: int, db: Session = Depends(get_db)):
    event_service.delete_event(db=db, event_id=event_id)
