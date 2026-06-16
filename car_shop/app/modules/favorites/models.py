from sqlalchemy.orm import Mapped,mapped_column

from sqlalchemy import ForeignKey,DateTime
from sqlalchemy.dialects.postgresql import UUID

from database.config import Base
from datetime import datetime,timezone
import uuid

class Favorite(Base):
    __tablename__ = "favorites"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4)

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        index=True)
    
    car_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("cars.id"),
        index=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Favorite(id={self.id},user_id={self.user_id},car_id={self.car_id})>"