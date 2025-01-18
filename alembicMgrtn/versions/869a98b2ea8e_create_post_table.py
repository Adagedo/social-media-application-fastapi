"""create post table

Revision ID: 869a98b2ea8e
Revises: 
Create Date: 2025-01-18 11:10:43.774323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '869a98b2ea8e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("new_posts_table", 
                    sa.Column("id", 
                              sa.Integer, 
                                        nullable=False, 
                                                 primary_key=True), sa.Column("title", 
                                                                              sa.String(255), 
                                                                              nullable=False))
     


def downgrade() -> None:
    op.drop_table("new_posts_table")
    pass
