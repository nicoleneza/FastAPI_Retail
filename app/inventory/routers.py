from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.inventory.schemas import ProductCreate, ProductResponse,CategoryCreate,CategoryResponse
from app.inventory.services import create_product, create_category
from database import get_db

router = APIRouter()

@router.post("/products", response_model=ProductResponse)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product, db)

@router.post("/categories", response_model=CategoryResponse)
def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(category, db)