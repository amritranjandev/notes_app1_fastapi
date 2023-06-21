"""add apt col

Revision ID: 74600a42edca
Revises: 6926a0a723df
Create Date: 2023-06-21 18:33:17.501716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74600a42edca'
down_revision = '6926a0a723df'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('address', 'apt_num')
