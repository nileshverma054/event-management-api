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
    app_name: str = "Event Management Api"
    app_version: str = "0.0.1"
    docs_url: str = "/docs"
    redoc_url: str | None = None
    environment: str = "development"
    port: int = 8000
    log_level: LogLevel = LogLevel.DEBUG

    model_config = SettingsConfigDict(env_file="app/.env")


@lru_cache()
def get_config() -> Settings:
    return Settings()
