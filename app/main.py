from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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

templates = Jinja2Templates(directory="app/templates")


@app.get("/rapidoc", response_class=HTMLResponse, include_in_schema=False)
async def get_rapidoc(request: Request):
    return templates.TemplateResponse("rapidoc.html", {"request": request})


app.include_router(api_router)
