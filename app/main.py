from fastapi import FastAPI
from app.routes import healthcheck_route

from app.utils.config import get_config

config = get_config()

app = FastAPI(
    title=config.app_name,
    version=config.app_version,
    description="API to manage events.",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    contact={"name": "Nilesh Verma", "url": "https://github.com/nileshverma054"},
    docs_url=config.docs_url,
    redoc_url=config.redoc_url,
)

app.include_router(healthcheck_route.router)
