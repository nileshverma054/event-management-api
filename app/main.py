from fastapi import FastAPI

from app.utils.config import get_config
from app.routes import router as api_router

config = get_config()

app = FastAPI(
    title=config.app_name,
    version=config.app_version,
    description="The Event Management RESTful API is a server-side application that allows users to manage events. It provides endpoints for different access levels, allowing users to view events and administrators to manage them. Users can register for events, and administrators can add, remove, or edit events. The API supports search functionality, allowing users to search for events by title, date, or location.",
    license_info={
        "name": "Git Repository",
        "url": "https://github.com/nileshverma054/event-management-api",
    },
    docs_url=config.docs_url,
    redoc_url=config.redoc_url,
)

app.include_router(api_router, prefix="/api")
