from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


from enum import Enum


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Settings(BaseSettings):
    APP_NAME: str = "Event Management API"
    APP_VERSION: str = "0.0.1"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    ENVIRONMENT: str = "development"
    PORT: int = 8000
    LOG_LEVEL: LogLevel = LogLevel.DEBUG
    DB_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_config() -> Settings:
    return Settings()
