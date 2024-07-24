from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.event_model import EventModel
from app.models.registration_model import RegistrationModel
from app.schemas.event_schema import (
    EventCreateRequestSchema,
    EventUpdateRequestSchema,
    RegisterEventResponseSchema,
)
from app.utils.logger import logger


def validate_event(db: Session, event_id: int):
    db_event = EventModel.get_by_id(db, event_id)
    logger.debug(f"db_event: {db_event}")
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


def get_event(db: Session, event_id: int):
    logger.info(f"Fetching event with ID: {event_id}")
    return EventModel.get_by_id(db, event_id)


def get_events(
    db: Session,
    title: str | None = None,
    date: str | None = None,
    location: str | None = None,
    skip: int = 0,
    limit: int = 10,
) -> list[EventModel]:
    logger.info(
        f"Fetching events: title: {title}, date: {date}, location: {location}, skip: {skip}, limit: {limit}"
    )
    query = db.query(EventModel)
    if title:
        query = query.filter(EventModel.title.ilike(f"%{title}%"))
    if date:
        query = query.filter(func.date(EventModel.date) == date)
    if location:
        query = query.filter(EventModel.location.ilike(f"%{location}%"))
    events = query.offset(skip).limit(limit).all()
    logger.debug(f"events: {events}")
    return events


def create_event(db: Session, event: EventCreateRequestSchema) -> EventModel:
    logger.info(f"Creating new event: {event}")
    db_event = EventModel(**event.model_dump())
    db_event.save(db)
    db.refresh(db_event)
    logger.info(f"Event created successfully: {db_event}")
    return db_event


def delete_event(db: Session, event_id: int) -> None:
    db_event = validate_event(db, event_id)
    logger.info(f"Deleting event: {db_event}")
    db_event.delete(db)
    logger.info("Event deleted successfully")


def update_event(db: Session, event_id: int, event: EventUpdateRequestSchema) -> EventModel:
    db_event = validate_event(db, event_id)
    payload = event.model_dump(exclude_unset=True)
    logger.debug(f"update event body: {payload}")
    for key, value in payload.items():
        logger.debug(f"key: {key}, value: {value}")
        setattr(db_event, key, value)
    db.flush()
    db.refresh(db_event)
    logger.info("Event updated successfully")
    return db_event


def register_event(db: Session, event_id: int, user_id: int) -> RegisterEventResponseSchema:
    logger.debug(f"event_id: {event_id}, user_id: {user_id}")
    db_event = validate_event(db, event_id)
    db_registration = RegistrationModel(user_id=user_id, event_id=event_id)
    db_registration.save(db)
    db.refresh(db_event)
    logger.info(f"Event registered successfully: {db_registration}")
    return RegisterEventResponseSchema(registration_id=db_registration.id)
