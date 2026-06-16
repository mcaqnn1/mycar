from sqlalchemy.orm import (
    Mapped,mapped_column,
    relationship)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import (
    String,ForeignKey,
    Integer,Text,
    Boolean,DateTime)

from database.config import Base
from typing import Optional
from datetime import datetime,timezone

import uuid

class Car(Base):
    __tablename__ = "cars"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4)

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        index=True)

    city_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("cities.id"),
        index=True)

    brand: Mapped[str] = mapped_column(
        String(100),nullable=False,index=True)

    model: Mapped[str] = mapped_column(
        String(100),nullable=False,index=True)

    mileage: Mapped[Optional[int]] = mapped_column(
        Integer,nullable=True)

    description: Mapped[Optional[str]] = mapped_column(
        Text,nullable=False)

    is_active: Mapped[bool] = mapped_column(
        Boolean,default=True)

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,default=False)

    created_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc))

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc),
        onupdate=lambda:datetime.now(timezone.utc))

    owner = relationship("User",back_populates="cars")

    def __repr__(self) -> str:
        return f"<Car(id={self.id},brand={self.brand},model={self.model})>"
    

    

    
    

    