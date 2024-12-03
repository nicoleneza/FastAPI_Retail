from datetime import datetime
from database import Base 
from typing import Optional, List

class ProductCreate(Base):
    name: str
    category_id: int
    sku: int
    description:str
    price:float
    stock_quantity:float
    created_at : Optional[datetime] = None
    updated_at : Optional[datetime] = None
    
class ProductResponse(Base):
    id: int 
    name: str
    category_id: int
    sku: int
    description: str
    price: float
    stock_quantity: float
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    class Config:
        orm_mode = True
    
class CategoryCreate(Base):
    name: str
   
class CategoryResponse(Base):
    id: int
    name: str
    class Config:
        orm_mode = True