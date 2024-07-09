from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.event_model import EventModel
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


def get_events(db: Session, skip: int = 0, limit: int = 10):
    logger.info("Fetching events")
    return db.query(EventModel).offset(skip).limit(limit).all()


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
