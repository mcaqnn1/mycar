from pydantic import BaseModel
import uuid

class FavoriteBase(BaseModel):
    user_id: uuid.UUID
    car_id: uuid.UUID

class FavoriteCreate(FavoriteBase):
    pass