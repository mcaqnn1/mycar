from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST:str
    DB_PORT:int
    DB_USER:str
    DB_PASSWORD:str
    DB_NAME:str
    DB_POOL_SIZE:int
    DB_MAX_OVERFLOW:int
    DB_POOL_PRE_PING:bool

    REDIS_HOST:str
    REDIS_PORT:int

    SMTP_HOST:str
    SMTP_PORT:int
    SMTP_USER:str
    SMTP_PASS:str

    model_config = SettingsConfigDict(env_file=".env",extra="ignore")

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

settings = Settings()
