# models/event.py

from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    location = Column(String)
    date = Column(DateTime)
