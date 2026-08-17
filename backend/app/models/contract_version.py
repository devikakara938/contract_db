from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.database import Base


class ContractVersion(Base):
    __tablename__ = "contract_versions"

    id = Column(Integer, primary_key=True, index=True)

    contract_id = Column(
        Integer,
        ForeignKey("contracts.id"),
        nullable=False
    )

    version_number = Column(
        Integer,
        nullable=False
    )

    changes = Column(String(500))

    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    contract = relationship(
        "Contract",
        back_populates="versions"
    )

    user = relationship(
        "User"
    )