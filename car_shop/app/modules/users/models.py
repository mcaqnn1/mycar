from sqlalchemy.orm import (
    Mapped,mapped_column,
    relationship)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String,DateTime,Boolean

from database.config import Base
from datetime import datetime,timezone
from modules.cars.models import Car

from typing import Optional
import uuid

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,index=True,
        default=uuid.uuid4)

    phone_number: Mapped[Optional[str]] = mapped_column(
        String(25),unique=True,
        nullable=True,index=True)

    email: Mapped[str] = mapped_column(
        String(75),unique=True,
        nullable=False)

    hashed_password: Mapped[str] = mapped_column(
        String,nullable=False)

    full_name: Mapped[str] = mapped_column(
        String,nullable=False,
        index=True)

    is_active: Mapped[bool] = mapped_column(
        Boolean,default=True)

    is_verified: Mapped[bool] = mapped_column(
        Boolean,default=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc))

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc),
        onupdate=lambda:datetime.now(timezone.utc))

    cars = relationship("Car",back_populates="owner")

    def __repr__(self) -> str:
        return f"<User(id={self.id},name={self.full_name})>"

    




    