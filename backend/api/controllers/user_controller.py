from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.database import get_session
from resources.users.user_service import UserService
from resources.users.user_schema import UserCreate, UserUpdate, UserResponse
from fastapi.security import HTTPBasicCredentials
from core.security import authenticate_user, create_access_token, Token
from core.deps import get_current_active_admin, get_current_active_user
from core.config import settings
from core.error_handlers import HTTPError
from datetime import timedelta


router = APIRouter()


@router.post("/",
             response_model=UserResponse,
             status_code=status.HTTP_201_CREATED,
             responses={
                 400: {"description": "Bad Request", "model": HTTPError},
                 401: {"description": "Unauthorized", "model": HTTPError},
                 403: {"description": "Forbidden", "model": HTTPError}
             })
def create_user(
    user: UserCreate,
    db: Session = Depends(get_session),
):
    service = UserService(db)
    return service.create_user(user)


@router.get("/", response_model=List[UserResponse],
            responses={
                 400: {"description": "Bad Request", "model": HTTPError},
             })
def read_users(skip: int = 0,
               limit: int = 10,
               db: Session = Depends(get_session),
               current_user=Depends(get_current_active_admin)
               ):
    service = UserService(db)
    return service.get_users(skip, limit)

@router.post("/login", response_model=Token,
                          responses={
                 400: {"description": "Bad Request", "model": HTTPError},
             })
def login_for_access_token(form_data: HTTPBasicCredentials = Depends(), db: Session = Depends(get_session)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"username": user.username, "is_admin": bool(user.is_admin), # type: ignore
              "is_active": bool(user.is_active)}, expires_delta=access_token_expires # type: ignore
    )
    return access_token
