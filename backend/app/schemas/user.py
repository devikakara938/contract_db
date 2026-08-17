from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = None
    name: str | None = None
    department: str | None = None
    salary: str | None = None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str | None = None
    department: str | None = None
    salary: str | None = None
    role: str

    class Config:
        from_attributes = True