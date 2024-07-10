import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.utils.constants import UserRoleEnum
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
        return f"<UserModel {self.id} {self.email}>"


class UserRoleModel(Base):
    __tablename__ = "user_role"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    role = Column(Enum(UserRoleEnum), nullable=False)

    user = relationship("UserModel", back_populates="roles")

    def __repr__(self):
        return f"<UserRoleModel {self.user_id} {self.role}>"
