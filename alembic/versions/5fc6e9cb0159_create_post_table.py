"""create post table

Revision ID: 5fc6e9cb0159
Revises: b84dba938db3
Create Date: 2021-11-11 05:58:13.372911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fc6e9cb0159'
down_revision = 'b84dba938db3'
branch_labels = None
depends_on = None




def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True,unique=True),
        sa.Column('title', sa.String(100)),
        sa.Column('body',sa.String(1000)),
        sa.Column('owner_id',sa.Integer),
        sa.Column('is_active',sa.Boolean),
        sa.Column('created_date',sa.DateTime)
    )


def downgrade():
    pass
