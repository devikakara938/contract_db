"""Add remaining ContractIQ tables

Revision ID: 91ca2f543ca3
Revises: 7b7a2bdbef26
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "91ca2f543ca3"
down_revision: Union[str, Sequence[str], None] = "7b7a2bdbef26"
branch_labels = None
depends_on = None


def upgrade() -> None:

    # Contract Versions
    op.create_table(
        "contract_versions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "contract_id",
            sa.Integer(),
            sa.ForeignKey("contracts.id"),
            nullable=False
        ),
        sa.Column("version_number", sa.Integer(), nullable=False),
        sa.Column("changes", sa.String(500)),
        sa.Column(
            "created_by",
            sa.Integer(),
            sa.ForeignKey("users.id"),
            nullable=False
        ),
    )

    # Renewals
    op.create_table(
        "renewals",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "contract_id",
            sa.Integer(),
            sa.ForeignKey("contracts.id"),
            nullable=False
        ),
        sa.Column("renewal_date", sa.Date()),
        sa.Column("status", sa.String(50), nullable=False),
    )

    # Notifications
    op.create_table(
        "notifications",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "contract_id",
            sa.Integer(),
            sa.ForeignKey("contracts.id"),
            nullable=False
        ),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id"),
            nullable=False
        ),
        sa.Column("message", sa.String(500)),
        sa.Column("status", sa.String(50), nullable=False),
    )

    # Reports
    op.create_table(
        "reports",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "contract_id",
            sa.Integer(),
            sa.ForeignKey("contracts.id"),
            nullable=False
        ),
        sa.Column(
            "generated_by",
            sa.Integer(),
            sa.ForeignKey("users.id"),
            nullable=False
        ),
        sa.Column("report_type", sa.String(100)),
        sa.Column("status", sa.String(50), nullable=False),
    )

    # Audit Logs
    op.create_table(
        "audit_logs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "contract_id",
            sa.Integer(),
            sa.ForeignKey("contracts.id"),
            nullable=False
        ),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id"),
            nullable=False
        ),
        sa.Column("action", sa.String(100), nullable=False),
        sa.Column("description", sa.String(500)),
    )

    # Activities
    op.create_table(
        "activities",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "contract_id",
            sa.Integer(),
            sa.ForeignKey("contracts.id"),
            nullable=False
        ),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id"),
            nullable=False
        ),
        sa.Column("activity_type", sa.String(100), nullable=False),
        sa.Column("description", sa.String(500)),
    )


def downgrade() -> None:

    op.drop_table("activities")
    op.drop_table("audit_logs")
    op.drop_table("reports")
    op.drop_table("notifications")
    op.drop_table("renewals")
    op.drop_table("contract_versions")