from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user_model import UserModel, UserRoleModel
from app.schemas.user_schema import UserCreateSchema, UserRoleCreateSchema
from app.utils.auth_utils import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
)
from app.utils.logger import logger



def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def create_user(db: Session, user: UserCreateSchema):
    logger.debug(f"create user: {user}")
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
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f"User created successfully with id: {db_user.id}")
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_email(db, username)
    logger.debug(f"user: {user}")
    if user and verify_password(password, user.hashed_password):
        return user
    return None


def create_user_role(db: Session, user_id: int, role: UserRoleCreateSchema):
    logger.debug(f"user_id: {user_id}, role: {role}")
    db_user_role = UserRoleModel(user_id=user_id, role=role.role.value)
    db.add(db_user_role)
    db.commit()
    db.refresh(db_user_role)
    logger.info(f"User role created successfully with id: {db_user_role.id}")
    return db_user_role


def create_tokens(user: UserModel):
    access_token = create_access_token(
        {
            "sub": user.email,
            "user_id": user.id,
            "roles": [role.role for role in user.roles],
        }
    )
    refresh_token = create_refresh_token(
        {
            "sub": user.email,
            "user_id": user.id,
        }
    )
    return {"access_token": access_token, "refresh_token": refresh_token}
