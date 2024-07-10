from fastapi import APIRouter

from app.routes.healthcheck_route import router as healthcheck_router
from app.routes.event_route import router as event_router
from app.routes.auth_route import router as auth_router

router = APIRouter()
router.include_router(healthcheck_router)
router.include_router(auth_router)
router.include_router(event_router)
