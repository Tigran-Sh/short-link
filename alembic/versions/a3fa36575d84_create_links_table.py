"""create links table

Revision ID: a3fa36575d84
Revises: 
Create Date: 2023-12-27 16:46:13.272730

"""
from typing import Sequence, Union

from sqlalchemy import func

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'a3fa36575d84'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'links',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, autoincrement=True, ),
        sa.Column('full_url', sa.String(length=255)),
        sa.Column('short_url', sa.String(length=64), unique=True),
        sa.Column('created_at', sa.DateTime(), server_default=func.now()),
        sa.Column('updated_at', sa.DateTime()),
    )


def downgrade() -> None:
    op.drop_table('links')
