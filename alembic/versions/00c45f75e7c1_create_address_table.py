"""Create address table

Revision ID: 00c45f75e7c1
Revises: 69473999e14b
Create Date: 2023-06-21 11:28:08.567849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00c45f75e7c1'
down_revision = '69473999e14b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(),
                              nullable=False),
                    sa.Column('address2', sa.String(),
                              nullable=False),
                    sa.Column('city', sa.String(),
                              nullable=False),
                    sa.Column('country', sa.String(),
                              nullable=False),
                    sa.Column('postalcode', sa.String(),
                              nullable=False)

                    )


def downgrade() -> None:
    op.drop_table('address')
