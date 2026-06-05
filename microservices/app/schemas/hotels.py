from pydantic import BaseModel

class SchemaHotels(BaseModel):
    id:int
    name:str
    location:str
    services:dict
    room_quantity:int

    model_config = {
        "from_attributes": True
    }
