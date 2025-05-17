
# app/schemas.py

from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    email: str


class NotificationCreate(BaseModel):
    user_id: int
    content: str

class Notification(BaseModel):
    id: int
    user_id: int
    content: str
    is_read: bool

class User(BaseModel):
    id: int
    name: str
    email: str
    notifications: List[Notification] = []

    class Config:
        orm_mode = True