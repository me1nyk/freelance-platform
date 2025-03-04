"""Add title to requests

Revision ID: a5444be897bd
Revises: de7ad429cca4
Create Date: 2025-02-16 12:34:52.610770

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'a5444be897bd'
down_revision: Union[str, None] = 'de7ad429cca4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('title', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('requests', 'title')
    # ### end Alembic commands ###
