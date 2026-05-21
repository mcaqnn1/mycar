from sqlmodel import SQLModel,Field
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func,DateTime,Column,String
import uuid
import datetime

class User(SQLModel,table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
            UUID(as_uuid=True),
            primary_key=True,
            nullable=False
        )
    )

    name: str = Field(
        sa_column=Column(
            String(120),
            nullable=False
        )
    )

    email: str = Field(
        sa_column=Column(
            String(255),
            unique=True,
            nullable=False,
            index=True
        )
    )

    password: str = Field(
        sa_column=Column(String(255),nullable=False)
    )

    created_at: datetime.datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False
        )
    )

    updated_at: datetime.datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False
        )
    )