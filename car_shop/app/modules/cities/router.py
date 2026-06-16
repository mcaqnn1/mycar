from fastapi import (
    APIRouter,HTTPException,
    status,Depends)

from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CityCreate
from typing import Annotated

from database.config import get_session
from .repository import CityRepository

import uuid

router = APIRouter(
    prefix="/cities",
    tags=["Cities"]
)

@router.post("/")
async def create_city(
    city:CityCreate,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = CityRepository(db)

    await repo.create(city_in=city)
    await db.commit()

    return city

@router.get("/all/")
async def get_all_cities(
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = CityRepository(db)

    cities = await repo.cities()

    return cities

@router.get("/{city_id}/")
async def get_city(
    city_id:uuid.UUID,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = CityRepository(db)

    city = await repo.get_by_id(city_id)

    if not city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="City not found!"
        )

    return city
