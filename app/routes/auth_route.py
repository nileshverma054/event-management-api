from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from app.schemas.user_schema import (
    UserCreateResponseSchema,
    UserCreateSchema,
    UserRoleCreateSchema,
    LoginResponseSchema
)
from app.services.user_service import (
    authenticate_user,
    create_tokens,
    create_user,
    create_user_role,
)
from app.utils.constants import UserRoleEnum
from app.utils.database import get_db
from app.utils.logger import logger

router = APIRouter(tags=["Authentication"])


@router.post(
    "/signup", response_model=UserCreateResponseSchema, status_code=HTTP_201_CREATED
)
def register_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    logger.debug(f"user: {user}")
    db_user = create_user(db, user)
    user_role = UserRoleCreateSchema(role=UserRoleEnum.user)
    create_user_role(db, db_user.id, user_role)
    return {"id": db_user.id}


@router.post("/login", response_model=LoginResponseSchema)
def login_user(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    logger.debug(f"user: {user}")
    user = authenticate_user(db, user.username, user.password)
    logger.debug(f"authenticated user: {user}")
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    tokens = create_tokens(user)
    return tokens
