from fastapi import (
    HTTPException,
    Request,status,Depends
)

from jose import jwt,JWTError

from dotenv import load_dotenv
import os

from datetime import datetime,timezone
from crud.models import UsersDAO

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def get_token(request:Request):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No token!"
        )
    return token

async def get_current_user(token:str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token=token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        expire = payload.get("exp")

        if not expire:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No expire"
            )

        if float(expire) < datetime(timezone.utc).timestamp():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token expired!"
            )

        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No user_id"
            )
    except JWTError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )

    user = await UsersDAO.find_one_or_none(id=user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No user"
        )
    
    return user