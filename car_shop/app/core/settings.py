from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    DB_HOST:str
    DB_PORT:int
    DB_USER:str
    DB_PASSWORD:str
    DB_NAME:str
    DB_POOL_SIZE:int
    DB_MAX_OVERFLOW:int
    DB_POOL_PRE_PING:bool

    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int

    ENCRYPTION_KEY:str

    REDIS_HOST:str
    REDIS_PORT:int

    SMTP_HOST:str
    SMTP_PORT:int
    SMTP_USER:str
    SMTP_PASS:str

    model_config = SettingsConfigDict(
        env_file=".env",
        enable_decoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"

@lru_cache
def get_settings():
    return Settings()