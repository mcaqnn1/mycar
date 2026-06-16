from pydantic import BaseModel
from typing import Optional
import uuid

class CarBase(BaseModel):
    user_id:uuid.UUID
    city_id:uuid.UUID

class CarCreate(CarBase):
    brand:str
    model:str
    mileage: Optional[int] = None
    description: Optional[str] = None
