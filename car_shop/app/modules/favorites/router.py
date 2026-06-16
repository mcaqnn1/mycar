from fastapi import APIRouter,HTTPException,status,Depends
from .repository import FavoriteRepository
from .schemas import FavoriteCreate
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from database.config import get_session
from modules.users.repository import UserRepository
from modules.cars.repository import CarRepository

router = APIRouter(
    prefix="/favs",
    tags=["Favorites"]
)

@router.post("/create/")
async def create_favorite(
    fav_in:FavoriteCreate,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo_user = UserRepository(db)
    repo_car = CarRepository(db)
    repo_fav = FavoriteRepository(db)

    user = await repo_user.get_by_id(fav_in.user_id)

    car = await repo_car.get_by_id(fav_in.car_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )

    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car not found!"
        )

    favorite = await repo_fav.create(fav_in)
    await db.commit()

    return favorite

@router.get("/all/")
async def get_favorites(
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = FavoriteRepository(db)

    favorites = await repo.favorites()

    return favorites