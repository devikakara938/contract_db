from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models
from backend.schemas import obligation as obligation_schema

router = APIRouter(prefix="/obligations", tags=["Obligations"])

@router.post("/", response_model=obligation_schema.Obligation)
def create_obligation(obligation: obligation_schema.ObligationCreate, db: Session = Depends(get_db)):
    db_obligation = models.Obligation(**obligation.dict())
    db.add(db_obligation)
    db.commit()
    db.refresh(db_obligation)
    return db_obligation

@router.get("/", response_model=list[obligation_schema.Obligation])
def get_obligations(db: Session = Depends(get_db)):
    return db.query(models.Obligation).all()