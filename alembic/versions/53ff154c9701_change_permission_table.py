"""Change permission table

Revision ID: 53ff154c9701
Revises: 87efaaf35a55
Create Date: 2025-02-17 22:12:22.557892

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '53ff154c9701'
down_revision: Union[str, None] = '87efaaf35a55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('permissions', 'can_manage_users',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('permissions', 'can_manage_requests',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('permissions', 'can_manage_requests',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('permissions', 'can_manage_users',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
