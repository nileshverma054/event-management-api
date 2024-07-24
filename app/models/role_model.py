import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Session

from app.utils.constants import UserRoleEnum as RoleEnum
from app.utils.database import Base


class UserRoleModel(Base):
    __tablename__ = "user_role"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)

    user = relationship("UserModel", back_populates="roles")

    def __repr__(self):
        return f"<UserRoleModel(id={self.id}, user_id={self.user_id}, role={self.role})>"


class RoleModel(db.Model):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())

    permissions = db.relationship(
        "PermissionModel",  # model to reference
        secondary="role_permission",  # association table
        backref=db.backref(
            # create a virtual attribute in PermissionModel with name roles.
            "roles",
            # lazy dynamic means child objects will not be loaded and returns qeury object
            lazy="dynamic",
        ),
        cascade="all",
    )

    def __repr__(self):
        return f"<Role name:{self.name}>"