"""user_email table

Revision ID: 164a738ab372
Revises: 
Create Date: 2020-08-17 00:19:42.372596
Revision by: premkumar30

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '164a738ab372'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_email',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('primary_email', sa.String(255), nullable=False, unique=True),
        sa.Column('secondary_email', sa.String(255), unique=True)
    )


def downgrade():
    op.drop_table('user_email')
