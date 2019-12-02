"""empty message

Revision ID: 85d2dac534c2
Revises: e3549d4f40c4
Create Date: 2019-09-24 15:36:23.938628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85d2dac534c2'
down_revision = 'e3549d4f40c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project') as batch_op:
        batch_op.drop_column('modified_author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('modified_author', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
