from core.database.config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,String,Integer,JSON

class Hotels(Base):
    __tablename__ = "hotels"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    location = Column(String,nullable=False)
    services = Column(JSON)
    room_quantity = Column(Integer,nullable=False)
    rooms = relationship("Rooms",back_populates="hotels")