from pydantic import BaseModel
import uuid

class CarImageBase(BaseModel):
    car_id:uuid.UUID

class CarImageCreate(CarImageBase):
    image_url:str
    position:int