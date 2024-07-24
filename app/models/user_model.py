import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship

from app.utils.database import Base


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String())
    is_active = Column(Boolean, default=True)
    role_id = Column(Integer, ForeignKey("role.id"))
    created_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
    )
    modified_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
    )

    role = relationship("RoleModel", back_populates="users")

    def __repr__(self):
        return f"<UserModel(id={self.id}, email={self.email})>"

    @classmethod
    def get_by_email(cls, db: Session, email: str):
        return db.query(cls).filter(cls.email == email).first()
