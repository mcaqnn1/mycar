from fastapi import (
    APIRouter,Depends,
    HTTPException,status,
    Response)

from .repository import UserRepository

from .schemas import (
    UserCreate,UserLogin,
    UserUpdatePhoneNumber,
    UserUpdateEmail,UserUpdateFullName)

from sqlalchemy.ext.asyncio import AsyncSession
from database.config import get_session
from api.deps import get_current_user,authenticate_user

from core.security import create_access_token
from fastapi_cache.decorator import cache

from tasks.task import send_email
from random import randint
from typing import Annotated
import uuid


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get(
        "/me/",
        summary="Get current user",
        description="Returns the authenticated user's profile")
async def get_me(current_user = Depends(get_current_user)):
    return current_user

@router.get(
        "/",
        summary="Get all users")
@cache(expire=30)
async def get_all_users(
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = UserRepository(db)

    users = await repo.all()
    return users

@router.get("/{user_id}/")
async def get_by_id(
    user_id:uuid.UUID,
    db: Annotated[AsyncSession,Depends(get_session)]
):
    repo = UserRepository(db)

    user = await repo.get_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )

    return user

@router.post(
        "/registration/",
        summary="User registration",
        description="Creates a new user account and stores the user's credentials in the system.")
async def register_user(
    user:UserCreate,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = UserRepository(db)

    password = randint(1111,9999)

    existing_user = await repo.check(user.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists!"
        )

    send_email(
        to_email=user.email,
        subject="Account Confirmation",
        body=f"Password:{password}"
    )

    await repo.create(user)

    await db.commit()


    return {
        "user":user.full_name,
        "message":"Successful!"
    }

@router.post(
        "/login/",
        summary="User login",
        description="Authenticates a user and returns an access token for authorized access.")
async def login_user(
    response:Response,
    user_log:UserLogin,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    user = await authenticate_user(user_log.email,user_log.password,db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found!"
        )
    access_token = create_access_token({"sub":str(user.id)})
    response.set_cookie(
        "access_token",
        access_token,
        httponly=True
    )
    return access_token

@router.get(
        "/{user_id}/cars/",
        summary="Get user with cars",
        description="Return user data together with associated cars")
@cache(expire=30)
async def get_car(
    user_id:uuid.UUID,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = UserRepository(db)
    user_car = await repo.get_user_with_car(user_id=user_id)
    return user_car

@router.post(
        "/signout/",
        summary="User sign out",
        description="Logs out the authenticated user by clearing the authentication cookie.")
async def sign_out(response:Response):
    response.delete_cookie("access_token")

    return {
        "message":"Deleted!"
    }

@router.put(
        "/{user_id}/phone_number/",
        summary="Update Phone Number",
        description="Updates users's phone number by user ID")
async def upd_phone_number(
    user_id:uuid.UUID,
    user:UserUpdatePhoneNumber,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = UserRepository(db)

    await repo.update_phone_number(user_id,user)
    await db.commit()

    return {
        "message":"Phone number updated!"
    }

@router.put(
        "/{user_id}/email/",
        summary="Update email",
        description="Updates user's email by user ID.")
async def upd_email(
    user_id:uuid.UUID,
    user:UserUpdateEmail,
    db: Annotated[AsyncSession,Depends(get_session)]
):
    repo = UserRepository(db)

    await repo.update_email(user_id,user)
    await db.commit()

    return {
        "message":"Email updated!"
    }

@router.put(
        "/{user_id}/full_name/",
        summary="Update full name",
        description="Updates user's full name by user ID.")
async def upd_full_name(
    user_id:uuid.UUID,
    user:UserUpdateFullName,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = UserRepository(db)

    await repo.update_full_name(user_id,user)
    await db.commit()

    return {
        "message":"Full name updated!"
    }

@router.delete("/delete/{user_id}/")
async def delete(
    user_id:uuid.UUID,
    db:Annotated[AsyncSession,Depends(get_session)]
):
    repo = UserRepository(db)

    await repo.delete(user_id)
    await db.commit()

    return {
        "message":"Deleted!"
    }
