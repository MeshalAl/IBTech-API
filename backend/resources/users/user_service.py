from typing import Sequence
from sqlalchemy.orm import Session
from .user_dal import UserDAL
from .user_schema import UserCreate, UserUpdate
from .user_model import User

class UserService:
    def __init__(self, db_session: Session) -> None:
        self.dal = UserDAL(db_session)

    def create_user(self, user_create: UserCreate) -> User:
        return self.dal.create_user(user_create)

    def get_user(self, user_id: int) -> User | None:
        return self.dal.get_user(user_id)

    def get_user_by_username(self, username: str) -> User | None:
        return self.dal.get_user_by_username(username)

    def get_users(self, skip: int = 0, limit: int = 10) -> Sequence[User]:
        return self.dal.get_users(skip, limit)

    def update_user(self, user_id: int, user_update: UserUpdate) -> User | None:
        return self.dal.update_user(user_id, user_update)

    def delete_user(self, user_id: int) -> User | None:
        return self.dal.delete_user(user_id)
    
