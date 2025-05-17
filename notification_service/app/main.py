# main.py

from fastapi import FastAPI ,HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import engine ,SessionLocal
from fastapi import Depends
from typing import List


# Create the tables if not already created
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    db=SessionLocal()\
        
    try:
        yield db
    finally:
        db.close()
        
@app.post("/usercreate",response_model=schemas.UserCreate)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
      db_user = models.User(name=user.name, email=user.email)
      db.add(db_user)
      db.commit()
      db.refresh(db_user)
      return db_user
  
@app.post("/notifications",response_model=schemas.Notification)
def send_noti(notification:schemas.NotificationCreate,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == notification.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Create notification\
    new_notification=models.Notification(
        user_id=notification.user_id,
        content=notification.content,
        is_read=False
    )
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification

@app.get("/users/{user_id}/notifications", response_model=list[schemas.Notification])
def get_user_notifications(user_id: int, db: Session = Depends(get_db)):
    notifications = db.query(models.Notification).filter(models.Notification.user_id == user_id).all()
    return notifications

@app.put("/notifications/{notification_id}/read", response_model=schemas.Notification)
def mark_notification_as_read(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    notification.is_read = True
    db.commit()
    db.refresh(notification)
    return notification

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@app.get("/users", response_model=List[schemas.User])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
