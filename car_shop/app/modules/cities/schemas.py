from pydantic import BaseModel

class CityBase(BaseModel):
    name: str

class CityCreate(CityBase):
    pass