from fastapi import FastAPI

from app.routes import api_router
from app.utils.config import get_config

config = get_config()

app = FastAPI(
    title=config.APP_NAME,
    version=config.APP_VERSION,
    description="""The Event Management RESTful API is a server-side application
    that allows users to manage events. It provides endpoints for different access levels,
    allowing users to view events and administrators to manage them. Users can register
    for events, and administrators can add, remove, or edit events.
    The API supports search functionality, allowing users to search for events
    by title, date, or location.""",
    license_info={
        "name": "Git Repository",
        "url": "https://github.com/nileshverma054/event-management-api",
    },
    contact={
        "name": "Nilesh Verma",
        "url": "https://github.com/nileshverma054",
        "email": "abc@example.com",
    },
    docs_url=config.DOCS_URL,
    redoc_url=config.REDOC_URL,
)

app.include_router(api_router)
