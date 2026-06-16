from sqlalchemy.ext.asyncio import AsyncSession
from .models import City
from .schemas import CityCreate
from sqlalchemy import select
import uuid

class CityRepository:
    def __init__(self,db:AsyncSession):
        self.db = db

    async def create(self,city_in:CityCreate):
        city = City(**city_in.model_dump())
        self.db.add(city)
        await self.db.flush()
        return city


    async def cities(self):
        query = await self.db.execute(select(City))
        return list(query.scalars().all())

    async def get_by_id(self,city_id:uuid.UUID):
        query = await self.db.execute(select(City).where(City.id == city_id))

        city = query.scalar_one_or_none()
        return city