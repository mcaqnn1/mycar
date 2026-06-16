from fastapi import (
    Request,HTTPException,
    status,Depends)

from sqlalchemy.ext.asyncio import AsyncSession
from database.config import get_session
from jose import jwt,JWTError

from datetime import datetime,timezone
from modules.users.repository import UserRepository
from pydantic import EmailStr
from core.security import verify_password

from core.settings import get_settings
import uuid

settings = get_settings()

def get_token(request:Request) -> str:
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No Token!"
        )

    return token

async def get_current_user(
    token: str = Depends(get_token),
    db:AsyncSession = Depends(get_session)
):
    try:
        payload = jwt.decode(
            token=token,
            key=settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        expire = payload.get("exp")

        if not expire:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No expire!"
            )

        if float(expire) < datetime.now(timezone.utc).timestamp():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token expired"
            )

        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No user_id!"
            )

    except JWTError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )

    user = await UserRepository(db).get_by_id(uuid.UUID(user_id))

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No user!"
        )
    return user

async def authenticate_user(
        email:EmailStr,
        password:str,
        db:AsyncSession = Depends(get_session)):
    user = await UserRepository(db).check(email)

    if not user or not verify_password(password,user.hashed_password):
        return None
    return user

        


    
