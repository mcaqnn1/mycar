from core.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from typing import AsyncGenerator
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=False,
    pool_pre_ping=settings.DB_POOL_PRE_PING,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncGenerator[AsyncSession,None]:
    async with AsyncSessionLocal() as session:
        yield session
