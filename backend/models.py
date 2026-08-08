from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    party_name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    obligations = relationship("Obligation", back_populates="contract")


class Obligation(Base):
    __tablename__ = "obligations"

    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"))
    description = Column(String)
    due_date = Column(Date)

    contract = relationship("Contract", back_populates="obligations")
    compliances = relationship("Compliance", back_populates="obligation")


class Compliance(Base):
    __tablename__ = "compliances"

    id = Column(Integer, primary_key=True, index=True)
    obligation_id = Column(Integer, ForeignKey("obligations.id"))
    status = Column(String)
    proof = Column(String)

    obligation = relationship("Obligation", back_populates="compliances")