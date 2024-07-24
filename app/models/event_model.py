from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import Session

from app.models.base_model import BaseModel


class EventModel(BaseModel):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True, nullable=False)
    description = Column(String(500))
    location = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Event(id={self.id} title={self.title})>"

    @classmethod
    def get_by_id(cls, db: Session, id: int):
        return db.query(cls).filter(cls.id == id).first()
