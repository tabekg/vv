"""empty message

Revision ID: d946256ebaed
Revises: 2bd07ec935e8
Create Date: 2019-05-03 22:06:04.229402

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd946256ebaed'
down_revision = '2bd07ec935e8'
branch_labels = None
depends_on = None
import app


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nc_users', sa.Column('attempts', app.JsonEncodedDict(), nullable=True))
    op.add_column('nc_users', sa.Column('last_attempt', app.JsonEncodedDict(), nullable=True))
    op.drop_column('nc_users', 'picture')
    op.drop_column('nc_users', 'last_time')
    op.add_column('users', sa.Column('last_time', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(length=35), nullable=False))
    op.add_column('users', sa.Column('picture', sa.String(length=55), nullable=True))
    op.add_column('users', sa.Column('surname', sa.String(length=35), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'surname')
    op.drop_column('users', 'picture')
    op.drop_column('users', 'name')
    op.drop_column('users', 'last_time')
    op.add_column('nc_users', sa.Column('last_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('nc_users', sa.Column('picture', sa.VARCHAR(length=55), autoincrement=False, nullable=True))
    op.drop_column('nc_users', 'last_attempt')
    op.drop_column('nc_users', 'attempts')
    # ### end Alembic commands ###