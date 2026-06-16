from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CarCreate
from .models import Car
from sqlalchemy import select
import uuid

class CarRepository:
    def __init__(self,db:AsyncSession):
        self.db = db

    async def create(self,car_in:CarCreate):
        car = Car(**car_in.model_dump())

        self.db.add(car)
        await self.db.flush()
        return car

    async def cars(self):
        query = await self.db.execute(select(Car))

        return query.scalars().all()

    async def get_by_id(self,id:uuid.UUID):
        query = await self.db.execute(
            select(Car)
            .where(Car.id == id))

        return query.scalar_one_or_none()