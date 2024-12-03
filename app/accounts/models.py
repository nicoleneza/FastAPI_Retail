from sqlalchemy import Column, Integer, String, Boolean, Table, DateTime, ForeignKey,Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from database import Base
from passlib.context import CryptContext

# Password hashing context
pw_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

class User(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer,primary_key=True)
    username = Column(String(225),unique=True,nullable=False)
    email = Column(String(233), unique=True, nullable=False)
    password = Column(String(225),nullable=False)
    user_type = Column(String(225),nullable=False)
    phone_number = Column(String(225))
    address = Column(Text)
    is_active = Column(Boolean,default=True)
    is_staff = Column(Boolean,default=False)

    
    def set_password(self,password):
        self.password = pw_context.hash(password)

    def check_password(self,password):
        return pw_context.verify(password,self.password)
    
# class UserProfile(Base):
#     __tablename__ = 'user_profile'

#     id = Column(Integer,primary_key=True)
#     user_id = Column(Integer,ForeignKey('auth_user.id'))
#     user_type = Column(String(225),default='customer')
#     phone_number = Column(String(225))
#     address = Column(Text)
#     points = Column(Integer,default=0)

#     user = relationship('User',back_populates='profile')

#     def __str__(self):
#         return f"{self.user.username} ({self.user_type})"

#     def add_points(self, amount):
#         """Add points based on purchase amount"""
#         new_points = int(amount * 10)  # $1 = 10 points
#         self.points += new_points
#         return new_points

