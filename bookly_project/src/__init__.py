from fastapi import FastAPI
import logging
from books.routes import router
from contextlib import asynccontextmanager
from database.main import conn_db
import uvicorn

version = "v1"

logger = logging.getLogger("uvicorn")

@asynccontextmanager
async def lifespan(app:FastAPI):

    logger.info("Server is starting...")
    await conn_db()

    yield

    logger.info("Server has been stopped")
    
app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
    lifespan=lifespan
)

app.include_router(
    router,
    prefix = f"/api/{version}/books",
    tags=["Books"]
)

if __name__ == '__main__':
    uvicorn.run("__init__:app",port=8000,reload=True)