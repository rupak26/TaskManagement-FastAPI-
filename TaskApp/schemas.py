import email
from pydoc import describe
from token import OP
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    username : str 
    email : str 
    password : str 

class showUser(BaseModel):
    username : str 
    email : str 
    
    class config:
        orm_mode = True
        
class Tasks(BaseModel):
    title : str 
    description : str 

    
class TasksPatch(BaseModel):
    title : Optional[str] = None 
    description : Optional[str] = None 


class showTask(BaseModel):
    title : str 
    description : str   
    created_at: datetime
    updated_at : datetime
    creator : Optional[showUser]
    
    class config:
        orm_mode = True

#Using username instend of email for deflault OAuth2PasswordRequestForm structure
class Login(BaseModel):
     username : str 
     password : str 


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email : Optional[str] = None