from fastapi import FastAPI
from routes.user import router as user_router
from contextlib import asynccontextmanager
from service.core.db import conn_db
import uvicorn
import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app:FastAPI):
    await conn_db()
    logger.info("Database connected")

    yield

    logger.info("Database disconnected")

app = FastAPI(
    title="Microservice",
    lifespan=lifespan
)
app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)






