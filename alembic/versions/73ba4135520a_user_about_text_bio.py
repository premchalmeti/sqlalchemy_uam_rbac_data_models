"""user (about_text->bio)

Revision ID: 73ba4135520a
Revises: d3292bedd611
Create Date: 2020-08-18 01:18:54.733326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73ba4135520a'
down_revision = 'd3292bedd611'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'user', 'about_text', new_column_name='bio', existing_type=sa.Text
    )


def downgrade():
    op.alter_column(
        'user', 'bio', new_column_name='about_text', existing_type=sa.Text
    )
