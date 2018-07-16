"""empty message

Revision ID: a6496088d1be
Revises: a31c2026b8c5
Create Date: 2018-07-16 01:33:51.534595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6496088d1be'
down_revision = 'a31c2026b8c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assetlocation',
    sa.Column('pri_id', sa.INTEGER(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('description', sa.VARCHAR(length=30), nullable=True),
    sa.Column('data_time', sa.TIMESTAMP(), nullable=True),
    sa.Column('longitude', sa.DECIMAL(precision=18, scale=12), nullable=True),
    sa.Column('latitude', sa.DECIMAL(precision=18, scale=12), nullable=True),
    sa.Column('elevation', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('pri_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assetlocation')
    # ### end Alembic commands ###