from pydantic import BaseModel,Field,EmailStr

class UserBase(BaseModel):
    phone_number: str
    email: EmailStr = Field(...,min_length=5)
    is_active: bool = True

class UserCreate(UserBase):
    password:str = Field(...,min_length=5)
    full_name:str = ""

class UserUpdatePhoneNumber(BaseModel):
    phone_number: str

class UserUpdateEmail(BaseModel):
    email: EmailStr

class UserUpdateFullName(BaseModel):
    full_name:str = ""

class UserLogin(BaseModel):
    email:EmailStr
    password:str