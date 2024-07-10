from sqlalchemy import Column, DateTime, Integer, String
from app.utils.database import Base


class EventModel(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True, nullable=False)
    description = Column(String(500))
    location = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)
