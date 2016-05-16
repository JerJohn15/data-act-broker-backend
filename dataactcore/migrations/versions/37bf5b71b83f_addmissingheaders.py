"""addMissingHeaders

Revision ID: 37bf5b71b83f
Revises: 6015ec0f59c9
Create Date: 2016-03-22 12:24:54.141000

"""

# revision identifiers, used by Alembic.
revision = '37bf5b71b83f'
down_revision = '6015ec0f59c9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('headers_missing', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'headers_missing')
    ### end Alembic commands ###


def upgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###

def upgrade_validation():
    pass

def downgrade_validation():
    pass

def upgrade_staging():
    pass

def downgrade_staging():
    pass