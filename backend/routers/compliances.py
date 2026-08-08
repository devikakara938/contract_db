from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models
from backend.schemas import compliance as compliance_schema

router = APIRouter(prefix="/compliances", tags=["Compliances"])

@router.post("/", response_model=compliance_schema.Compliance)
def create_compliance(compliance: compliance_schema.ComplianceCreate, db: Session = Depends(get_db)):
    db_compliance = models.Compliance(**compliance.dict())
    db.add(db_compliance)
    db.commit()
    db.refresh(db_compliance)
    return db_compliance

@router.get("/", response_model=list[compliance_schema.Compliance])
def get_compliances(db: Session = Depends(get_db)):
    return db.query(models.Compliance).all()