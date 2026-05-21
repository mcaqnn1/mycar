from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession

from service.core.db import get_session
from service.core.schemas import UserCreate,UserRead
from service.security.password import hashed_password
from service.core.models import User
from sqlalchemy import select
import uuid


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/",response_model=dict)
async def create_user(data: UserCreate,session: AsyncSession = Depends(get_session)):
    user = User(
        name=data.name.strip().title(),
        email=data.email,
        password=hashed_password(data.password)
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return {
        "id":  str(user.uid),
        "message": "created"
    }

@router.get("/{user_id}/",response_model=UserRead)
async def get_user(user_id: uuid.UUID,session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(User).where(User.uid == user_id)
    )

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user


