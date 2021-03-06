"""add

Revision ID: 65202482f0b6
Revises: 7578de759f8e
Create Date: 2019-03-25 17:14:27.955204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65202482f0b6'
down_revision = '7578de759f8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=30), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('good_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['good_id'], ['goods.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###
