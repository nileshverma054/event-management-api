import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.utils.database import Base


class RegistrationModel(Base):
    __tablename__ = "event_registration"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    event_id = Column(Integer, ForeignKey("event.id"))
    is_deleted = Column(Boolean, default=False)
    created_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
    )

    user = relationship("UserModel")
    event = relationship("EventModel")

    def __repr__(self):
        return f"RegistrationModel(id={self.id}, user_id={self.user_id}, event_id={self.event_id})"
