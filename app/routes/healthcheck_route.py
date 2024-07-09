from fastapi import APIRouter

from app.schemas.heathcheck_schema import HealthCheckResponse

router = APIRouter(tags=["Healthcheck"])


@router.get("/healthcheck", response_model=HealthCheckResponse)
def healthcheck():
    return {"status": "ok"}
