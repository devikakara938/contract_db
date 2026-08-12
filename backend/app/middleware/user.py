from sqlalchemy import Column, Integer, String, DateTime
from backend.app.database_old import Base # IKKADA IMPORTANT
from datetime import datetime

class User(Base):  # Base ni inherit cheyyali
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)