from fastapi import APIRouter
from modules.users.router import router as user_router
from modules.cities.router import router as city_router
from modules.cars.router import router as car_router
from modules.car_images.router import router as car_image_router
from modules.favorites.router import router as favorite_router


api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(city_router)
api_router.include_router(car_router)
api_router.include_router(car_image_router)
api_router.include_router(favorite_router)
