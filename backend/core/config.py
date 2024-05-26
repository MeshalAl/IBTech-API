from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = Field(..., env="DATABASE_URL")
    secret_key: str = Field(..., env="SECRET_KEY")
    access_token_expire_minutes: int = 30
    debug: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

try:
    settings = Settings()
except ValidationError as e:
    print("Environment variables are not set correctly:", e)
