from sqlmodel import SQLModel
from pydantic import EmailStr
from typing import Optional

class UserCreate(SQLModel):
    name: str
    email: EmailStr
    password: str

class UserRead(SQLModel):
    uid: str
    name: str
    email: EmailStr
    created_at: Optional[str] = None
    updated_at: Optional[str] = None