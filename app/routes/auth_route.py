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

# @router.post("/token/refresh")
# def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
#     payload = decode_token(refresh_token)
#     if not payload:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
#     user = get_user_by_username(db, payload.get("sub"))
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
#     tokens = create_tokens(user)
#     return tokens

# @router.post("/admin/create_role")
# def create_role(user_role: UserRoleCreate, user_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_admin_user)):
#     db_user_role = create_user_role(db, user_id, user_role)
#     return db_user_role
