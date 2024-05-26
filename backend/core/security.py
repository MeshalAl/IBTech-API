from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .config import settings
from resources.users.user_model import User
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from db.database import get_session
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"
SECRET_KEY = settings.secret_key
bearer_scheme = HTTPBearer()


class Token(BaseModel):
    access_token: str
    token_type: str


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    access_token = Token(access_token=encoded_jwt, token_type="bearer")
    return access_token


def authenticate_user(db: Session, username: str, password: str) -> User | bool:
    from resources.users.user_service import UserService
    user_service = UserService(db)

    user = user_service.get_user_by_username(username)
    if not user or not verify_password(password, str(user.hashed_password)):
        return False
    return user


def get_current_user(token: HTTPAuthorizationCredentials = Depends(bearer_scheme),
                     db: Session = Depends(get_session)) -> User | None:
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        if payload:
            from resources.users.user_service import UserService
            user_service = UserService(db)
            username: str = payload.get("username")
            user = user_service.get_user_by_username(username)
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return user
        return
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")
