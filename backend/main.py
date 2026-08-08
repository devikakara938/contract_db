from .routers import contracts,obligations,compliances,users
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="ContractIQ Backend")

@app.get("/")
def home():
    return {"message": "ContractIQ Backend is Running 🚀"}

@app.post("/employees/")
def create_employee(name: str, email: str, db: Session = Depends(database.get_db)):
    db_employee = models.Employee(name=name, email=email)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/employees/")
def get_employees(db: Session = Depends(database.get_db)):
    return db.query(models.Employee).all()
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database
from .routers import contracts, obligations, compliances  # 1. routers import cheyi

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="ContractIQ Backend")

# Home route
@app.get("/")
def home():
    return {"message": "ContractIQ Backend is Running 🚀"}

# Employee routes - nee daggara already undi
@app.post("/employees/")
def create_employee(name: str, email: str, db: Session = Depends(database.get_db)):
    db_employee = models.Employee(name=name, email=email)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/employees/")
def get_employees(db: Session = Depends(database.get_db)):
    return db.query(models.Employee).all()

# 2. Ivi kothaga add cheyi - Contract, Obligation, Compliance routers
app.include_router(contracts.router)
app.include_router(obligations.router)
app.include_router(compliances.router)
app.include_router(users.router)