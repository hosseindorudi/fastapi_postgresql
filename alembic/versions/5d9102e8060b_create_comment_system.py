"""create comment system

Revision ID: 5d9102e8060b
Revises: 7d323ec0f5cd
Create Date: 2021-11-11 07:17:34.974690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d9102e8060b'
down_revision = '7d323ec0f5cd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer, primary_key=True,unique=True),
        sa.Column('name', sa.String(100)),
        sa.Column('email', sa.String(1000)),
        sa.Column('body',sa.String(1000)),
        sa.Column('post_id',sa.Integer),
        sa.Column('is_active',sa.Boolean),
        sa.Column('created_date',sa.DateTime)
    )


def downgrade():
    pass
