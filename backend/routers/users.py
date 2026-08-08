from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database, schemas

router = APIRouter(prefix="/users", tags=["Users"])

# 1. GET by ID
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.Employee).filter(models.Employee.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 2. UPDATE
@router.put("/{user_id}")
def update_user(user_id: int, user_data: schemas.EmployeeCreate, db: Session = Depends(database.get_db)):
    user = db.query(models.Employee).filter(models.Employee.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.name = user_data.name
    user.email = user_data.email
    db.commit()
    db.refresh(user)
    return user

# 3. DELETE
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.Employee).filter(models.Employee.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}