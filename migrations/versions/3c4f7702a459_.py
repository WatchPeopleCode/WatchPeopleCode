"""empty message

Revision ID: 3c4f7702a459
Revises: 5a24a4aa5eb3
Create Date: 2015-07-10 23:59:20.856464

"""

# revision identifiers, used by Alembic.
revision = '3c4f7702a459'
down_revision = '5a24a4aa5eb3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'streamer_youtube_channel_key', 'streamer', type_='unique')
    op.drop_column('streamer', 'youtube_channel')
    op.drop_column('streamer', 'youtube_name')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('streamer', sa.Column('youtube_name', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    op.add_column('streamer', sa.Column('youtube_channel', sa.VARCHAR(length=24), autoincrement=False, nullable=True))
    op.create_unique_constraint(u'streamer_youtube_channel_key', 'streamer', ['youtube_channel'])
    ### end Alembic commands ###