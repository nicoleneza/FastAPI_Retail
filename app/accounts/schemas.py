from pydantic import EmailStr
from typing import Optional,List
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class UserCreate(Base):
    id:Mapped[str]= mapped_column(primary_key=True, autoincrement = True)
    username:Mapped[str]= mapped_column(unique=True,nullable=False)
    email: Mapped[str]= mapped_column(unique=True,nullable=False)
    password: Mapped[str]= mapped_column(nullable=False)
    user_type:Mapped[str]= mapped_column(nullable=False)
    phone_number: Mapped[Optional[str]] = mapped_column(default=datetime.utcnow)
    address:Optional[str]

class UserResponse(Base):
    id:int
    username:str
    email: EmailStr
    password:str
    user_type:str
    phone_number:Optional[str] = None
    address:Optional[str]

    class Config:
        orm_mode = True
        
class UserRead(Base):
    id: int
    username: str
    email: EmailStr
    password: str
    user_type: str
    
    
