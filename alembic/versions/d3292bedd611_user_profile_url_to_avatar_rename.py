"""User(profile_url to avatar) rename

Revision ID: d3292bedd611
Revises: 164a738ab372
Create Date: 2020-08-18 00:13:07.020460
Revision By: premkumar30
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3292bedd611'
down_revision = '164a738ab372'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'user', 'profile_url', new_column_name='avatar', existing_type=sa.Text
    )


def downgrade():
    op.alter_column(
        'user', 'avatar', new_column_name='profile_url', existing_type=sa.Text
    )
