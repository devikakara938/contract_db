"""add user table

Revision ID: ad11532e46ba
Revises: 00ff499bec93
Create Date: 2026-08-12 17:04:48.065735

"""

from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = 'ad11532e46ba'
down_revision: Union[str, Sequence[str], None] = '00ff499bec93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass