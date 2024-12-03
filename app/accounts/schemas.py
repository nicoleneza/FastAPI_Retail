from pydantic import EmailStr
from typing import Optional,List
from database import Base

class UserCreate(Base):
    username:str
    email:EmailStr
    password:str
    user_type:str
    phone_number:Optional[str] = None
    address:Optional[str]

class UserResponse(Base):
    id:int
    username:str
    email:EmailStr
    password:str
    user_type:str
    phone_number:Optional[str] = None
    address:Optional[str]

    class Config:
        orm_mode = True
    
