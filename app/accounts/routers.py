from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.accounts.schemas import UserCreate,UserResponse
from app.accounts.models import User
from app.accounts.services import create_user
from database import get_db

router = APIRouter()

@router.post('/register',response_model=UserResponse)
def register_user(user:UserCreate,db:Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400,detail='Email or password already exists')
    return create_user(user,db)
