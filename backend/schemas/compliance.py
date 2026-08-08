from pydantic import BaseModel
from typing import Optional

class ComplianceBase(BaseModel):
    obligation_id: int
    status: str
    proof: Optional[str] = None

class ComplianceCreate(ComplianceBase):
    pass

class Compliance(ComplianceBase):
    id: int

    class Config:
        from_attributes = True