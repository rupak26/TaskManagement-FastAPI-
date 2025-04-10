from ast import mod
from datetime import  timedelta 
from fastapi import APIRouter , Depends , HTTPException , status
from .. import models
from .. import schemas
from ..repository import user
from sqlalchemy.orm import Session 
from ..Database import get_db 
from ..hashing import Hasing
from .token import create_access_token , ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Authentication']
) 

@router.post('/registration', status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.UserSchema , db : Session = Depends(get_db)):
    return user.create_user(request , db)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends() , db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first() 
    if not user:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , 
                           detail= "email did not exists")
    if not Hasing.verify(request.password , user.password):
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , 
                           detail= "Incorrect Password") 
    #Generate Token 
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
           "email" : user.email,
           "user_id" : user.id ,
        }
    )
    return { "access_token" :access_token, "token_type" :"bearer"}