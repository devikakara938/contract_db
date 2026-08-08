from pydantic import BaseModel
from datetime import date
from typing import Optional

class ContractBase(BaseModel):
    title: str
    party_name: str
    start_date: date
    end_date: date

class ContractCreate(ContractBase):
    pass

class Contract(ContractBase):
    id: int

    class Config:
        from_attributes = True # v2 lo orm_mode