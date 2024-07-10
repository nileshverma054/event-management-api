from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.event_model import EventModel
from app.models.registration_model import RegistrationModel
from app.schemas.event_schema import EventCreateRequestSchema, EventUpdateRequestSchema
from app.utils.logger import logger


def validate_event(db: Session, event_id: int):
    db_event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


def get_event(db: Session, event_id: int):
    logger.info(f"Fetching event with ID: {event_id}")
    return db.query(EventModel).filter(EventModel.id == event_id).first()


def get_events(
    db: Session,
    title: str | None = None,
    date: str | None = None,
    location: str | None = None,
    skip: int = 0,
    limit: int = 10,
):
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
    return query.offset(skip).limit(limit).all()


def create_event(db: Session, event: EventCreateRequestSchema):
    logger.info(f"Creating new event: {event.title}")
    db_event = EventModel(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    logger.info(f"Event created successfully with id: {db_event.id}")
    return db_event


def delete_event(db: Session, event_id: int):
    db_event = validate_event(db, event_id)
    logger.info(f"Deleting event with ID: {event_id}")
    db.delete(db_event)
    db.commit()
    logger.info("Event deleted successfully")
    return db_event


def update_event(db: Session, event_id: int, event: EventUpdateRequestSchema):
    db_event = validate_event(db, event_id)
    payload = event.model_dump(exclude_unset=True)
    logger.debug(f"update event body: {payload}")
    for key, value in payload.items():
        logger.debug(f"key: {key}, value: {value}")
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)
    logger.info("Event updated successfully")
    return db_event


def register_event(db: Session, event_id: int, user_id: int):
    logger.debug(f"event_id: {event_id}, user_id: {user_id}")
    db_event = validate_event(db, event_id)
    db_registration = RegistrationModel(user_id=user_id, event_id=event_id)
    db.add(db_registration)
    db.commit()
    db.refresh(db_event)
    logger.info(f"Event registered successfully: {db_event}")
    return {"registration_id": db_registration.id}
