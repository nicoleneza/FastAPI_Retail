from sqlalchemy.orm import Session
from app.inventory.models import Product,Category
from app.inventory.schemas import ProductCreate,CategoryCreate,ProductRead
from fastapi import HTTPException

def create_category(category: CategoryCreate, db:Session):
    
    existing_category = db.query(Category).filter(Category.name == category.name).first()
    if existing_category:
        raise HTTPException(status_code=404, message="category already exists")
    db_category = Category(name = category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
def create_product(product: ProductCreate, db:Session):
    category = db.query(Category).filter(Category.id == product.category_id).first()
    if not category:
        raise HTTPException(status_code=404,message="Category not found")
    db_product = Product(
        name = product.name,
        category_id = product.category.id,
        sku= product.sku,
        description = product.description,
        price = product.price,
        stock_quantity = product.stock_quantity,
        created_at = product.created_at,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def retrieve_product(db:Session):
    product_list = db.query(Product).all()
    return [ProductRead.from_orm(product) for product in product_list]