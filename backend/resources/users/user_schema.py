from pydantic import BaseModel
from datetime import datetime
class UserBase(BaseModel):
    username: str | None = None
    is_active: bool | None = None
    is_admin: bool | None = None

class UserCreate(UserBase):
    username: str
    password: str

class UserUpdate(UserBase):
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: datetime | None
    
