from core.database.config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,ForeignKey,String,Float

class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer,primary_key=True)
    hotel_id = Column(Integer,ForeignKey("hotels.id"),nullable=False)
    name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    quantity = Column(String,nullable=False)
    hotels = relationship("Hotels",back_populates="rooms")