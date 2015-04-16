"""empty message

Revision ID: 45fdcd9ac732
Revises: 3acbc54c61e5
Create Date: 2015-04-10 14:58:10.070381

"""

# revision identifiers, used by Alembic.
revision = '45fdcd9ac732'
down_revision = '3acbc54c61e5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('streamer', sa.Column('test', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('streamer', 'test')
    ### end Alembic commands ###