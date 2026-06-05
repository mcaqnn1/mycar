from fastapi import (
    APIRouter,
    HTTPException,
    status,Response,
    Depends
)

from schemas.users import (
    SchemaUserRegister,
    SchemaUserLogin,
    SchemaUserUpdate,
    SchemaUserSendMessage
)

from crud.models import UsersDAO
from api.dependencies import get_current_user
from tasks.task import send_message_email

from core.auth.security import (
    get_password_hash,
    authenticate_user,
    create_access_token
)

import asyncio

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/register/")
async def register_user(user_data: SchemaUserRegister):
    existing_user = await UsersDAO.find_one_or_none(
        email=user_data.email
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists!"
        )
    
    password_hash = get_password_hash(user_data.password)

    await UsersDAO.add(
        full_name=user_data.full_name,
        email=user_data.email,
        hashed_password=password_hash
    )
    return {
        "message":"Registration successful!"
    }

@router.get("/all_users/")
async def all_users():
    result = await UsersDAO.find_all()
    return result

@router.post("/login/")
async def login_user(
    response:Response,
    user_data:SchemaUserLogin
):
    await asyncio.sleep(3)

    user = await authenticate_user(
        user_data.email,
        user_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    
    access_token = create_access_token({"exp":str(user.id)})
    response.set_cookie(
        "access_token",
        access_token,
        httponly=True
    )

    return {
        "message":"Successful!"
    }

@router.post("/sign_out/")
async def sign_out(response:Response):
    response.delete_cookie("access_token")

    return {
        "message":"Token deleted!"
    }

@router.put("/update/{user_id}/")
async def update_data(
    user_id:int,
    user_data:SchemaUserUpdate
):
    asyncio.sleep(3)

    ext_user = await UsersDAO.find_one_or_none(id=user_id)

    if not ext_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    password_hash = get_password_hash(user_data.password)

    await UsersDAO.update(
        id=user_id,
        full_name=user_data.full_name,
        email=user_data.email,
        hashed_password=password_hash
    )

    return {
        "message": "User updated successfully!"
    }

@router.delete("/delete/{user_id}/")
async def delete_user(user_id:int):
    await UsersDAO.delete(id=user_id)

    return {
        "message":"User deleted!"
    }

@router.get("/profile/")
async def get_profile(
    current_user = Depends(get_current_user)
):
    return current_user

@router.post("/message/")
async def send_message(user:SchemaUserSendMessage):
    send_message_email.delay(
        to_email=user.email,
        subject="Account Confirmation",
        body="Password:1234"
    )

    return {
        "message":"Sent!"
    }