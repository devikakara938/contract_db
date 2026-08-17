from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)

    contract_id = Column(
        Integer,
        ForeignKey("contracts.id"),
        nullable=False
    )

    generated_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    report_type = Column(String(100))

    status = Column(
        String(50),
        nullable=False
    )

    contract = relationship(
        "Contract",
        back_populates="reports"
    )

    user = relationship(
        "User"
    )