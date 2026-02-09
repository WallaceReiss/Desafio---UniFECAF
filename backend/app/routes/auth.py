from fastapi import APIRouter, Request
from app.core.security import create_token
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter(prefix="/auth", tags=["Auth"])
limiter = Limiter(key_func=get_remote_address)

@router.post("/login")
@limiter.limit("5/minute")
async def login(request: Request):
    token = create_token()
    return {"access_token": token}
