from fastapi import FastAPI
from modules.users.router import router as user_router
from modules.cities.router import router as city_router
from modules.cars.router import router as car_router
from modules.car_images.router import router as car_image_router
from modules.favorites.router import router as favorite_router
from core.redis import lifespan
import uvicorn

app = FastAPI(
    title="MyCar",
    lifespan=lifespan
)

app.include_router(user_router)
app.include_router(city_router)
app.include_router(car_router)
app.include_router(car_image_router)
app.include_router(favorite_router)

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)
