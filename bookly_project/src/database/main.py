from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from config import Config
from sqlmodel import SQLModel
from typing import AsyncGenerator


engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def conn_db():
    async with engine.begin() as conn:
        from database.models import Books
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncGenerator[AsyncSession,None]:
    async with AsyncSessionLocal() as session:
        yield session
