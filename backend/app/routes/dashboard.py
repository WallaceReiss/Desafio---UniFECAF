from fastapi import APIRouter, Depends, Request
from app.services.dashboard_service import get_dashboard_data
from app.schemas.dashboard_schema import DashboardResponse
from app.core.security import verify_token
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])
limiter = Limiter(key_func=get_remote_address)

@router.get("/", response_model=DashboardResponse, dependencies=[Depends(verify_token)])
@limiter.limit("10/minute")
async def get_dashboard(request: Request):
    return get_dashboard_data()
