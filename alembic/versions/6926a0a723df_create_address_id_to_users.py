"""Create address_id to users

Revision ID: 6926a0a723df
Revises: 00c45f75e7c1
Create Date: 2023-06-21 11:38:19.917530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6926a0a723df'
down_revision = '00c45f75e7c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column(
        'address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table='users', referent_table='address', local_cols=[
                          'address_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name='users')
    op.drop_column('users', 'address_id')
