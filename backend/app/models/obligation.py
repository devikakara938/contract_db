from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.database import Base


class Obligation(Base):
    __tablename__ = "obligations"

    id = Column(Integer, primary_key=True, index=True)

    contract_id = Column(
        Integer,
        ForeignKey("contracts.id"),
        nullable=False
    )

    assigned_to = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    description = Column(String(500))

    due_date = Column(Date)

    status = Column(
        String(50),
        nullable=False
    )

    contract = relationship(
        "Contract",
        back_populates="obligations"
    )

    user = relationship(
        "User"
    )