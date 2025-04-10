from ast import mod
from  sqlalchemy.orm import Session  
from .. import models
from .. import schemas
from fastapi import  status ,  HTTPException 
from datetime import datetime

def get_all(db : Session):
    return  db.query(models.Task).all() 
    

def get_by_id(id , db : Session):
    task = db.query(models.Task).filter(models.Task.id==id).first()
    if task is None:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , 
                           detail= f"Task with {id} did not exists")
    return task 


def individual_user_tasks(db : Session , id : int):
    task = db.query(models.Task).filter(models.Task.user_id==id).all()
    if task is None:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , 
                           detail= f"Task with {id} did not exists")
    return task 



def create_task(request:schemas.Tasks , db : Session , id : int):
    new_tasks = models.Task(title=request.title , description = request.description , user_id = id)
    new_tasks.created_at = datetime.utcnow()
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    return new_tasks

def delete_by_id(id : int , db : Session , user : int):
    task = db.query(models.Task).filter(models.Task.id==id).first()
    if task is None:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , 
                           detail= f"Tasks with {id} did not exists")
    
    if task.user_id != user:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized to delete this task")
    
    db.query(models.Task).filter(models.Task.id==id).delete(synchronize_session=False) 
    db.commit() 
    return ({'msg' : 'Task deleted'})

def updated_by_id(id:int , request:schemas.Tasks , db : Session , user : int):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if task.user_id != user:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized to update this task")
    
    db.query(models.Task).filter(models.Task.id == id).update(
        {
            "title": request.title,
            "description": request.description
        },
        synchronize_session=False
    )
    if not task:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                           detail= f"Tasks with {id} did not exists")
    task.updated_at = datetime.utcnow()
    db.commit() 
    return ({'msg' : 'Task updated'})

def updatedPartiali_by_id(id:int , request:schemas.TasksPatch , db : Session , user : int):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    
    if task.user_id != user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized to update this task")
    if not task:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                           detail= f"Task with {id} did not exists")
    if request.title is not None:
        task.title = request.title

    if request.description is not None:
        task.description = request.description
    
    task.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(task)
    return ({'msg' : 'Task updated'})