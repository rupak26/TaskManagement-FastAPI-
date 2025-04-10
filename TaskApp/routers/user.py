from .. import schemas
from ..Database import get_db
from .. import models
from fastapi import Depends, FastAPI , status , HTTPException , APIRouter
from sqlalchemy.orm import Session  
from ..hashing import Hasing
from typing import List
from ..repository import user

router = APIRouter(
    prefix= '/user',
    tags=['User'] 
) 


@router.get('/',status_code=status.HTTP_200_OK ,  response_model=List[schemas.showUser])
def show_user(db : Session = Depends(get_db)):
    return user.show_all_user(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,  response_model=schemas.showUser)
def show_user_by_id(id:int , db : Session = Depends(get_db)):
    return user.show_user_by_id(id , db)
