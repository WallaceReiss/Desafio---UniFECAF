from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "unifecaf-secret"
ALGORITHM = "HS256"

security = HTTPBearer()

def create_token():
    token = jwt.encode({"user": "aluno"}, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
