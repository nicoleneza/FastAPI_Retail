from sqlalchemy import Column, Integer, String, Text, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Product(Base):
    __tablename__ = "products",
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    sku = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    # reorder_level = Column(Integer, default=10, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Establish a relationship with the Category table
    category = relationship("Category", back_populates="products")
    
    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"

    @validates("stock_quantity")
    def validate_stock_quantity(self, key, value):
        if value < 0:
            raise ValueError("Stock quantity cannot be negative")
        return value

class Category(Base):
    __tablename__ = "categories"
    __allow_unmapped__ = True
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, unique=True)
    products = relationship("Product", back_populates="category")
