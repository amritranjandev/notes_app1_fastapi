"""create phone number for user col

Revision ID: 69473999e14b
Revises: 
Create Date: 2023-06-21 11:15:00.314381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69473999e14b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))


def downgrade() -> None:
    op.drop_column('users','phone_number')
