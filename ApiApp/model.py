from .db import Base
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Posts(Base):
    __tablename__ = "posts"
    _id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    published = Column(String(225), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    owner_id = Column(Integer, ForeignKey("users._id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class User(Base):
    __tablename__ = "users"
    _id = Column(Integer, nullable=False, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users._id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts._id", ondelete="CASCADE"), primary_key=True)
    
    
class Order(Base):
    __tablename__ = "orders"
    _id = Column(Integer, nullable=False, primary_key=True) 
    product = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))    
    
    
    
    
    
    