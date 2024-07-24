import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Session

from app.utils.constants import UserRoleEnum as RoleEnum
from app.utils.database import Base


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String())
    is_active = Column(Boolean, default=True)
    created_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
    )
    modified_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
    )
    roles = relationship("UserRoleModel", back_populates="user")

    def __repr__(self):
        return f"<UserModel(id={self.id}, email={self.email})>"

    @classmethod
    def get_by_email(cls, db: Session, email: str):
        return db.query(cls).filter(cls.email == email).first()


class RoleModel(Base):
    __tablename__ = "user_role"


class UserRoleModel(Base):
    __tablename__ = "user_role"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)

    user = relationship("UserModel", back_populates="roles")

    def __repr__(self):
        return f"<UserRoleModel(id={self.id}, user_id={self.user_id}, role={self.role})>"
