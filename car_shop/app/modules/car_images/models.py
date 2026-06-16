from sqlalchemy.orm import(
    Mapped,mapped_column,
    relationship)

from sqlalchemy import String,Integer,ForeignKey
from database.config import Base
from sqlalchemy.dialects.postgresql import UUID

from modules.cars.models import Car
import uuid

class CarImage(Base):
    __tablename__ = "car_images"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4)

    car_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("cars.id"),
        index=True)

    image_url: Mapped[str] = mapped_column(String,nullable=False)

    position: Mapped[int] = mapped_column(Integer,default=0)

    def __repr__(self):
        return f"<Car Image(id={self.id},url={self.image_url})>"
