from passlib.context import CryptContext
from datetime import datetime,timezone,timedelta
from .settings import get_settings
from cryptography.fernet import Fernet,InvalidToken
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = get_settings()

def get_password_hash(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY,
        settings.ALGORITHM
    )
    return encoded_jwt

def encrypt_name(name: str | None) -> str:
    try:
        f = Fernet(settings.ENCRYPTION_KEY.encode())
        return f.encrypt(name.encode()).decode()
    except InvalidToken:
        return name

def decrypt_name(name: str | None) -> str:
    try:
        f = Fernet(settings.ENCRYPTION_KEY.encode())
        return f.decrypt(name.encode()).decode()
    except InvalidToken:
        return name