from sqlalchemy.ext.asyncio import AsyncSession
from .models import Favorite
from .schemas import FavoriteCreate
from sqlalchemy import select

class FavoriteRepository:
    def __init__(self,db:AsyncSession):
        self.db = db

    async def create(self,favorite:FavoriteCreate):
        fav = Favorite(
            user_id=favorite.user_id,
            car_id=favorite.car_id
        )
        self.db.add(fav)
        await self.db.flush()
        return fav

    async def favorites(self):
        query = await self.db.execute(select(Favorite))
        return query.scalars().all()