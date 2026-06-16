from fastapi import APIRouter,HTTPException,status,Depends
from .schemas import CarImageCreate
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from database.config import get_session
from .repository import CarImageRepository
from modules.cars.repository import CarRepository
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/car_images",
    tags=["Car Images"]
)

@router.post("/")
async def create_img_car(
    img:CarImageCreate,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo_car = CarRepository(db)
    repo_car_img = CarImageRepository(db)

    car_id = await repo_car.get_by_id(img.car_id)

    if not car_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No car!"
        )
    await repo_car_img.create_image(img)
    await db.commit()

    return {
        "message":"Created!"
    }

@router.get("/all/")
@cache(expire=30)
async def all_car_images(
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = CarImageRepository(db)

    car_images = await repo.car_images()

    return car_images