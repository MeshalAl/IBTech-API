from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_session
from .security import get_current_user
from resources.users.user_model import User



def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active: # type: ignore
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_current_active_admin(current_user: User = Depends(get_current_active_user)) -> User:
    if not current_user.is_admin: # type: ignore
        raise HTTPException(status_code=403, detail="Not authorized")
    return current_user

