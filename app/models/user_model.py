import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship
from app.models.association_tables import role_permission_association
from app.utils.database import Base


class PermissionModel(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True)
    name = Column(
        String(255),
        index=True,
        doc="Represents the router function name defined under @router.",
    )
    description = Column(String(255))

    roles = relationship(
        "RoleModel",
        secondary=role_permission_association,
        back_populates="permissions",
    )

    def __repr__(self):
        return f"<PermissionModel(name={self.name})>"


class RoleModel(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    description = Column(String(255))

    permissions = relationship(
        "PermissionModel",
        secondary=role_permission_association,
        back_populates="roles",
    )
    users = relationship("UserModel", back_populates="role")

    def __repr__(self):
        return f"<RoleModel(name={self.name})>"

    @classmethod
    def get_by_name(cls, db: Session, name: str):
        return db.query(cls).filter(cls.name == name).first()


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
    def get_by_id(cls, db: Session, user_id: int):
        return db.query(cls).filter(cls.id == user_id).first()

    @classmethod
    def get_by_email(cls, db: Session, email: str):
        return db.query(cls).filter(cls.email == email).first()
