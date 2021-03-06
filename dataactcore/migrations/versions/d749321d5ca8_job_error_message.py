"""job_error_message

Revision ID: d749321d5ca8
Revises: b0445ef35b9a
Create Date: 2016-08-23 10:06:56.400162

"""

# revision identifiers, used by Alembic.
revision = 'd749321d5ca8'
down_revision = 'b0445ef35b9a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('error_message', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'error_message')
    ### end Alembic commands ###

