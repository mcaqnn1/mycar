from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from jose import jwt
from dotenv import load_dotenv
from pydantic import EmailStr
from crud.models import UsersDAO
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict) -> dict:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp":int(expire.timestamp())})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM
    )
    return encoded_jwt

async def authenticate_user(email:EmailStr,password:str):
    user  = await UsersDAO.find_one_or_none(email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user