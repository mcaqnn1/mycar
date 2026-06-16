from fastapi import FastAPI
from core.redis import lifespan
from api.v1.api import api_router
import uvicorn

app = FastAPI(
    title="MyCar",
    lifespan=lifespan
)
app.include_router(api_router,prefix="/api/v1")

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)
