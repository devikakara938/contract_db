"""sync database with current models

Revision ID: 353ca8ea7e28
Revises: 8ed8d78ad08b
Create Date: 2026-08-14 14:00:34.069068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '353ca8ea7e28'
down_revision: Union[str, Sequence[str], None] = '8ed8d78ad08b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
