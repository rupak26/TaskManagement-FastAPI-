from pydoc import describe
from .Database import Base 
from sqlalchemy import Column , Integer , String , ForeignKey , DateTime 
from sqlalchemy.orm import relationship 
from datetime import datetime

class Task(Base):
    __tablename__ = 'tasks' 
    
    id = Column(Integer , primary_key = True , index = True)
    title = Column(String(100))
    description = Column(String(200)) 
    user_id = Column(Integer , ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    creator = relationship("User" , back_populates="tasks")


class User(Base):
    __tablename__ = 'users' 

    id = Column(Integer , primary_key = True , index = True)
    username = Column(String(100))
    email = Column(String(200))
    password = Column(String(100)) 
    
    tasks = relationship("Task" , back_populates = "creator")