"""create posts table

Revision ID: 02056ba374ed
Revises: 
Create Date: 2021-12-20 03:26:40.168816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02056ba374ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_table('posts')
    pass
