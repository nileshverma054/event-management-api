import arguably
from pydantic import SecretStr
from getpass import getpass

# this is required to set python path
import evironment
import db_service

from app.utils.database import SessionLocal
from app.schemas.user_schema import UserCreateSchema


@arguably.command
def seed_db():
    """
    Seed the database
    """
    print("Seeding database..")
    db = SessionLocal()
    try:
        db_service.seed_db(db)
    finally:
        db.close()
    print("[OK] Database seeded..")


@arguably.command
def create_user(first_name: str, last_name: str, email: str, role: str = "admin"):
    """
    Create an user
    Args:
        first_name: first name of the user
        last_name: last name of the user
        email: email of the user
        password: password of the user
        role: role of the user
    """
    password = getpass(prompt="Enter password for user: ")
    print("Creating user..")
    db = SessionLocal()
    user = UserCreateSchema(
        first_name=first_name, last_name=last_name, email=email, password=SecretStr(password)
    )
    try:
        db_service.add_user(db, role, user)
    finally:
        db.close()
    print("[OK] User created..")


if __name__ == "__main__":
    arguably.run()
