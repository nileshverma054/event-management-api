from pydantic import BaseModel, EmailStr, Field, SecretStr

name_pattern = r"^[a-zA-Z]+$"


class UserBaseSchema(BaseModel):
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="The user's first name",
    )
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="The user's last name",
    )
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    password: SecretStr


class UserInDBSchema(UserBaseSchema):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class UserCreateResponseSchema(BaseModel):
    id: int


class LoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
