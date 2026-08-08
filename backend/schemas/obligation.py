from pydantic import BaseModel
from datetime import date
from typing import Optional

class ObligationBase(BaseModel):
    contract_id: int
    description: str
    due_date: Optional[date] = None

class ObligationCreate(ObligationBase):
    pass

class Obligation(ObligationBase):
    id: int

    class Config:
        from_attributes = True