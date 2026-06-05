from core.database.config import Base
from sqlalchemy import Column,Integer,String,Boolean,DateTime
from sqlalchemy.sql import func

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True)
    full_name = Column(String,nullable=False)
    email = Column(String,unique=True,nullable=False)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean,default=True)
    date_time = Column(DateTime(timezone=True),server_default=func.now())
    is_superuser = Column(Boolean,default=False)