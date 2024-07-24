from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, relationship

from app.models.association_tables import role_permission_association
from app.utils.database import Base


class RoleModel(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    description = Column(String(255))

    users = relationship("UserModel", back_populates="role")
    permissions = relationship(
        "PermissionModel",
        secondary=role_permission_association,
        back_populates="roles",
    )

    def __repr__(self):
        return f"<RoleModel(id={self.id}, name={self.name})>"

    @classmethod
    def get_by_name(cls, db: Session, name: str):
        return db.query(cls).filter(cls.name == name).first()
