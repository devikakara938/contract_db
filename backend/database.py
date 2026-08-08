from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.core.config import settings

# 1. Engine create
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True  # DB connection drop ayina malli connect avthundi
)

# 2. Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. IDI CHALA IMPORTANT - Base
#    Idi import chesi anni models inherit cheyyali
Base = declarative_base()

# 4. DB dependency - FastAPI routes lo use cheyyadaniki
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()