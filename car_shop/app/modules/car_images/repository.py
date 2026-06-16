from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CarImageCreate
from .models import CarImage
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import uuid

class CarImageRepository:
    def __init__(self,db:AsyncSession):
        self.db = db

    async def create_image(self,car_image_in:CarImageCreate):
        car_image = CarImage(**car_image_in.model_dump())

        self.db.add(car_image)
        await self.db.flush()

        return car_image

    async def car_images(self):
        query = await self.db.execute(select(CarImage))
        return query.scalars().all()
