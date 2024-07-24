from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

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
