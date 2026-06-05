from pydantic import BaseModel,EmailStr

class SchemaUserRegister(BaseModel):
    full_name:str
    email:EmailStr
    password:str

class SchemaUserLogin(SchemaUserRegister):
    pass

class SchemaUserUpdate(SchemaUserLogin):
    pass

class SchemaUserSendMessage(BaseModel):
    email: EmailStr