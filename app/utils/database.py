from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.utils.config import get_config
from app.utils.logger import logger

config = get_config()

engine = create_engine(config.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        logger.info(f"Performing database rollback due to exception: {e}")
        db.rollback()
        raise e
    finally:
        db.close()
