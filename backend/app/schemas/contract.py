from datetime import date, datetime
from pydantic import BaseModel


class ContractCreate(BaseModel):
    title: str
    contract_number: str
    category: str
    description: str | None = None
    start_date: date | None = None
    end_date: date | None = None


class ContractOut(BaseModel):
    id: int
    owner_id: int
    contract_number: str
    title: str
    category: str
    description: str | None
    start_date: date | None
    end_date: date | None
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True