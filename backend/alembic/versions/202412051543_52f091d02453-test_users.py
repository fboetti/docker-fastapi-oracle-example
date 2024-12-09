"""Test migration file

Revision ID: 52f091d02453
Revises: 
Create Date: 2024-12-05 15:43:24.382077+01:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52f091d02453'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'test_users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('first_name', sa.String(length=50), nullable=True),
        sa.Column('last_name', sa.String(length=50), nullable=True),
        sa.Column('gender', sa.Enum('male', 'female', 'other', name='usergender'), nullable=True),
        sa.Column('birth_year', sa.Integer(), nullable=True),
        sa.Column('email', sa.String(length=50), nullable=False),
        sa.Column('hashed_password', sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )


def downgrade() -> None:
    op.drop_index(op.f('ix_test_users_id'), table_name='test_users')
    op.drop_table('test_users')
