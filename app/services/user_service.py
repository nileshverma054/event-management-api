from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.role_model import RoleModel
from app.models.user_model import UserModel
from app.schemas.user_schema import UserCreateSchema
from app.utils.auth_utils import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
)
from app.utils.logger import logger


def get_user_by_email(db: Session, email: str) -> UserModel | None:
    return UserModel.get_by_email(db, email=email)


def validate_role(db: Session, role: str) -> RoleModel:
    db_role = RoleModel.get_by_name(db, name=role)
    if not db_role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid role",
        )
    return db_role


def create_user(db: Session, user: UserCreateSchema, role: str = "user") -> UserModel:
    logger.debug(f"create user: {user}, role: {role}")
    db_role = validate_role(db, role)
    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )
    hashed_password = hash_password(user.password.get_secret_value())
    db_user = UserModel(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=hashed_password,
        role_id=db_role.id,
    )
    db.add(db_user)
    db.flush()
    db.refresh(db_user)
    logger.info(f"User created successfully: {db_user}")
    return db_user


def authenticate_user(db: Session, username: str, password: str) -> UserModel | None:
    user = get_user_by_email(db, username)
    logger.debug(f"user: {user}")
    if user and verify_password(password, user.hashed_password):
        return user
    return None


def create_tokens(user: UserModel) -> dict[str, str]:
    access_token = create_access_token(
        {
            "sub": user.email,
            "user_id": user.id,
        }
    )
    refresh_token = create_refresh_token(
        {
            "sub": user.email,
            "user_id": user.id,
        }
    )
    return {"access_token": access_token, "refresh_token": refresh_token}
