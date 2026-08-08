from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models
from backend.schemas import contract as contract_schema

router = APIRouter(prefix="/contracts", tags=["Contracts"])

@router.post("/", response_model=contract_schema.Contract)
def create_contract(contract: contract_schema.ContractCreate, db: Session = Depends(get_db)):
    db_contract = models.Contract(**contract.dict())
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract

@router.get("/", response_model=list[contract_schema.Contract])
def get_contracts(db: Session = Depends(get_db)):
    return db.query(models.Contract).all()