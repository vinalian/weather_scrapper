"""Create database

Revision ID: 586d8d2b128f
Revises: 
Create Date: 2024-05-06 13:59:36.506371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '586d8d2b128f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('temperature', sa.FLOAT(), nullable=False),
    sa.Column('wind_speed', sa.FLOAT(), nullable=False),
    sa.Column('wind_direction', sa.FLOAT(), nullable=False),
    sa.Column('air_pressure', sa.FLOAT(), nullable=False),
    sa.Column('precipitation_type', sa.VARCHAR(length=32), nullable=False),
    sa.Column('precipitation_count', sa.FLOAT(), nullable=False),
    sa.Column('datetime', postgresql.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('datetime')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather')
    # ### end Alembic commands ###
