from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True