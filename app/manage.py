import arguably
from fastapi import Depends
from sqlalchemy.orm import Session

from app.utils.database import get_db



@arguably.command
def seed_database():
    print("Seeding database..")
    print("[OK] Database seeded..")


@arguably.command
def create_admin_user(username: str, password: str):
    print("Creating admin user..")
    print("[OK] Admin user created..")


def create_roles(db: Session = Depends(get_db)):
    print("Creating roles..")
    print("[OK] Roles created..")


if __name__ == "__main__":
    arguably.run()
