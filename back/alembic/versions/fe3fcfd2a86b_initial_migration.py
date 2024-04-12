"""Initial migration

Revision ID: fe3fcfd2a86b
Revises: 
Create Date: 2024-04-07 01:14:15.921545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe3fcfd2a86b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('status', sa.Enum('active', 'inactive', 'pending', name='userstatus'), server_default='pending', nullable=False),
    sa.Column('user_role', sa.Enum('master', 'admin', 'operator', name='userrole'), server_default='operator', nullable=False),
    sa.Column('creation_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('temperature_sensors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('temperature', sa.String(length=60), nullable=False),
    sa.Column('creation_date', sa.Date(), nullable=False),
    sa.Column('session_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['session_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('temperature_sensors')
    op.drop_table('users')
    # ### end Alembic commands ###
