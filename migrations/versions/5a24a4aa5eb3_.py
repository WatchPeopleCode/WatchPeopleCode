"""empty message

Revision ID: 5a24a4aa5eb3
Revises: 552800b5e708
Create Date: 2015-07-10 23:45:40.229999

"""

# revision identifiers, used by Alembic.
revision = '5a24a4aa5eb3'
down_revision = '552800b5e708'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('youtube_channel',
    sa.Column('channel_id', sa.String(length=24), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=True),
    sa.Column('streamer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['streamer_id'], ['streamer.id'], ),
    sa.PrimaryKeyConstraint('channel_id')
    )
    op.add_column(u'stream', sa.Column('youtube_channel_id', sa.String(length=24), nullable=True))
    op.create_foreign_key(None, 'stream', 'youtube_channel', ['youtube_channel_id'], ['channel_id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stream', type_='foreignkey')
    op.drop_column(u'stream', 'youtube_channel_id')
    op.drop_table('youtube_channel')
    ### end Alembic commands ###
