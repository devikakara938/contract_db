# 1. IDI FIRST 3 LINES GA ADD CHEYI
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# 2. TARVATA nee purana imports anni
from backend.database import Base
from backend.core.config import settings
from backend.models import Employee
target_metadata = Base.metadata

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# 3. Duplicate imports teeseyyi - Line 13,14,19-22 rendu sarlu unnayi
# # from app.database import Base  <- idi duplicate, delete cheyi
# # from app.core.config import settings <- idi kuda duplicate

config = context.config
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)