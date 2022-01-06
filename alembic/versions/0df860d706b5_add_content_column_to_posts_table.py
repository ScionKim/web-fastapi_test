"""add content column to posts table

Revision ID: 0df860d706b5
Revises: 02056ba374ed
Create Date: 2022-01-04 08:05:40.668772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0df860d706b5'
down_revision = '02056ba374ed'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
