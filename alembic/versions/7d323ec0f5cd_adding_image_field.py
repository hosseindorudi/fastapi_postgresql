"""adding image field

Revision ID: 7d323ec0f5cd
Revises: 5fc6e9cb0159
Create Date: 2021-11-11 06:21:05.930477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d323ec0f5cd'
down_revision = '5fc6e9cb0159'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('url',sa.String(200))
    )


def downgrade():
    pass