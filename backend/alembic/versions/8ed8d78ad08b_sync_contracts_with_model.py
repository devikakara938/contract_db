"""sync contracts with model

Revision ID: 8ed8d78ad08b
Revises: 6b1e88d1de2b
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8ed8d78ad08b"
down_revision: Union[str, Sequence[str], None] = "6b1e88d1de2b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add owner_id
    op.add_column(
        "contracts",
        sa.Column("owner_id", sa.Integer(), nullable=True)
    )

    # Add foreign key from contracts.owner_id to users.id
    op.create_foreign_key(
        "contracts_owner_id_fkey",
        "contracts",
        "users",
        ["owner_id"],
        ["id"]
    )

    # Add contract_number
    op.add_column(
        "contracts",
        sa.Column(
            "contract_number",
            sa.String(length=100),
            nullable=True
        )
    )

    # Add status
    op.add_column(
        "contracts",
        sa.Column(
            "status",
            sa.String(length=50),
            nullable=True
        )
    )


def downgrade() -> None:
    op.drop_constraint(
        "contracts_owner_id_fkey",
        "contracts",
        type_="foreignkey"
    )

    op.drop_column("contracts", "status")
    op.drop_column("contracts", "contract_number")
    op.drop_column("contracts", "owner_id")