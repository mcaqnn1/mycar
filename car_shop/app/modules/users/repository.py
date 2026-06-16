from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from core.security import encrypt_name,get_password_hash,decrypt_name
from .models import User
from .schemas import UserCreate,UserUpdatePhoneNumber,UserUpdateEmail,UserUpdateFullName
from pydantic import EmailStr
from sqlalchemy import select,update,delete
import uuid

class UserRepository:
    def __init__(self,db: AsyncSession):
        self.db = db

    async def check(self,user:EmailStr):
        query = await self.db.execute(select(User).where(User.email == user))
        return query.scalar_one_or_none()

    async def create(self,user_in:UserCreate) -> User:
        db_user = User(
            phone_number=user_in.phone_number,
            email=user_in.email,
            hashed_password=get_password_hash(user_in.password),
            full_name=encrypt_name(user_in.full_name)
        )
        self.db.add(db_user)
        await self.db.flush()
        return db_user

    async def all(self):
        query = await self.db.execute(select(User))
        return query.scalars().all()

    async def get_by_id(self,user_id:uuid.UUID):
        query = await self.db.execute(select(User).where(User.id == user_id))
        user = query.scalar_one_or_none()
        if user:
            user.full_name = decrypt_name(user.full_name)
        return user

    async def update_phone_number(self,user_id:uuid.UUID,user_ph:UserUpdatePhoneNumber):
        query = await self.db.execute(
            update(User)
            .where(User.id == user_id)
            .values(
                phone_number = user_ph.phone_number
            )
            .returning(User))

        await self.db.flush()
        return query.scalar_one_or_none()

    
    async def update_email(self,user_id:uuid.UUID,user_em:UserUpdateEmail):
        query = await self.db.execute(
            update(User)
            .where(User.id ==user_id)
            .values(
                email = user_em.email
            )
            .returning(User))

        await self.db.flush()
        return query.scalar_one_or_none()

    async def update_full_name(self,user_id:uuid.UUID,user_fn:UserUpdateFullName):
            query = await self.db.execute(
                update(User)
                .where(User.id ==user_id)
                .values(
                    full_name = encrypt_name(user_fn.full_name)
                )
                .returning(User))
    
            await self.db.flush()
            return query.scalar_one_or_none()

    async def delete(self,user_id:uuid.UUID):
        query = await self.db.execute(
            delete(User)
            .where(User.id == user_id)
            .returning(User))

        await self.db.flush()
        return query.scalar_one_or_none()

    async def get_user_with_car(self,user_id:uuid.UUID) -> User | None:
        query = await self.db.execute(
            select(User)
            .options(selectinload(User.cars))
            .where(User.id == user_id))

        return query.scalar_one_or_none()


