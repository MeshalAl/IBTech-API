from sqlalchemy.orm import Session
from typing import Sequence
from resources.users.user_model import User
from resources.users.user_schema import UserCreate, UserUpdate
from core.security import get_password_hash

class UserDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_user(self, user_create: UserCreate) -> User:
        hashed_password = get_password_hash(user_create.password)
        new_user = User(
            username=user_create.username,
            hashed_password=hashed_password,
            is_active=user_create.is_active or True,
            is_admin=user_create.is_admin or False
        )
        self.db_session.add(new_user)
        self.db_session.flush()
        self.db_session.refresh(new_user)
        return new_user

    def get_user(self, user_id: int) -> User | None:
        return self.db_session.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username: str) -> User | None:
        return self.db_session.query(User).filter(User.username == username).first()

    def get_users(self, skip: int = 0, limit: int = 10) -> Sequence[User]:
        return self.db_session.query(User).offset(skip).limit(limit).all()

    def update_user(self, user_id: int, user_update: UserUpdate) -> User | None:
        db_user = self.db_session.query(User).filter(User.id == user_id).first()
        if db_user:
            update_data = user_update.model_dump(exclude_unset=True)
            if 'password' in update_data:
                update_data['hashed_password'] = get_password_hash(update_data.pop('password'))
            for key, value in update_data.items():
                setattr(db_user, key, value)
            self.db_session.flush()
            self.db_session.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> User | None:
        db_user = self.db_session.query(User).filter(User.id == user_id).first()
        if db_user:
            self.db_session.delete(db_user)
            self.db_session.flush()
            return db_user
        return None
