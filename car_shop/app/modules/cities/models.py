from sqlalchemy.orm import (
    Mapped,mapped_column)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import String
from database.config import Base

import uuid

class City(Base): 
    __tablename__ = "cities"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,index=True)

    name: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        unique=True)

    def __repr__(self):
        return f"<City(id={self.id},name={self.name})>"