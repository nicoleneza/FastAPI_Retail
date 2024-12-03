from sqlalchemy.orm import Session
from app.accounts.models import User
from app.accounts.schemas import UserCreate

def create_user(user:UserCreate,db:Session):
    db_user= User(
        username = user.username,
        email=user.email,
        password = user.password,
        user_type=user.user_type,
        phone_number = user.phone_number,
        address = user.address
    )
    db_user.set_password(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

