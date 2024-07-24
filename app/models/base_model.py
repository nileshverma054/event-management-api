from sqlalchemy.orm import Session

from app.utils.database import Base


class BaseModel(Base):
    __abstract__ = True

    def save(self, db: Session) -> None:
        """Save the object to the database."""
        db.add(self)
        db.flush()

    def delete(self, db: Session) -> None:
        """Delete the object from the database."""
        db.delete(self)
        db.flush()

    @classmethod
    def get_all(cls, limit=10):
        """Get all records from the table."""
        return cls.query.limit(limit).all()
