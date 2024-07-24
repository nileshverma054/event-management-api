from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.schema import Table

from app.utils.database import Base

role_permission_association = Table(
    "role_permission",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("role.id")),
    Column("permission_id", Integer, ForeignKey("permission.id")),
)
