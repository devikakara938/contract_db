from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.models.contract import Contract
from backend.app.models.user import User
from backend.app.schemas.contract import ContractCreate, ContractOut
from backend.app.core.auth import get_current_user


router = APIRouter()


# CREATE CONTRACT
@router.post(
    "/",
    response_model=ContractOut,
    status_code=status.HTTP_201_CREATED
)
def create_contract(
    contract: ContractCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    # Find logged-in user
    user = db.query(User).filter(
        User.email == current_user["email"]
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Check duplicate contract number
    existing = db.query(Contract).filter(
        Contract.contract_number == contract.contract_number
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Contract number already exists"
        )

    # Create contract
    db_contract = Contract(
        owner_id=user.id,
        contract_number=contract.contract_number,
        title=contract.title,
        category=contract.category,
        description=contract.description,
        start_date=contract.start_date,
        end_date=contract.end_date,
        status="Draft"
    )

    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)

    return db_contract


# GET ALL CONTRACTS
@router.get(
    "/",
    response_model=list[ContractOut]
)
def get_contracts(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    contracts = db.query(Contract).all()

    return contracts


# GET CONTRACT BY ID
@router.get(
    "/{contract_id}",
    response_model=ContractOut
)
def get_contract(
    contract_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    contract = db.query(Contract).filter(
        Contract.id == contract_id
    ).first()

    if not contract:
        raise HTTPException(
            status_code=404,
            detail="Contract not found"
        )

    return contract