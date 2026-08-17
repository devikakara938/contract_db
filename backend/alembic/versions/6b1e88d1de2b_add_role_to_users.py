"""Add role to users

Revision ID: 6b1e88d1de2b
Revises: 91ca2f543ca3
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "6b1e88d1de2b"
down_revision: Union[str, Sequence[str], None] = "91ca2f543ca3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "role",
            sa.String(length=50),
            nullable=False,
            server_default="Employee"
        )
    )


def downgrade() -> None:
    op.drop_column("users", "role")