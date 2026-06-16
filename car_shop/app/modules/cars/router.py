from fastapi import (
    APIRouter,HTTPException,
    status,Depends)

from .schemas import CarCreate
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from database.config import get_session

from .repository import CarRepository
from modules.users.repository import UserRepository
from modules.cities.repository import CityRepository

from fastapi_cache.decorator import cache
import uuid


router = APIRouter(
    prefix="/cars",
    tags=["Cars"]
)

@router.post(
        "/",
        summary="Create car with user and city validation",
        description="Create car with user and city validation")
async def create_car(
    car_create:CarCreate,
    db:Annotated[AsyncSession,Depends(get_session)]
):

    repo_user = UserRepository(db)
    repo_city = CityRepository(db)
    repo_car = CarRepository(db)

    user = await repo_user.get_by_id(car_create.user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )

    city = await repo_city.get_by_id(car_create.city_id)

    if not city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="City not found!"
        )

    await repo_car.create(car_in=car_create)
    await db.commit()

    return {
        "message":"Car created!"
    }

@router.get("/all/")
@cache(expire=30)
async def get_all_cars(
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = CarRepository(db)
    cars = await repo.cars()

    return cars

@router.get("/{car_id}/")
@cache(expire=30)
async def get_car(
    car_id:uuid.UUID,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = CarRepository(db)

    car = await repo.get_by_id(car_id)

    return car



    