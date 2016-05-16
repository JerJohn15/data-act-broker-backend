"""adding incorrect password attempt to user model

Revision ID: ac6c35049702
Revises: 2701ef6ccb69
Create Date: 2016-05-02 14:11:50.161182

"""

# revision identifiers, used by Alembic.
revision = 'ac6c35049702'
down_revision = '9a47fb5fac41'
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
    pass
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
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
    op.add_column('users', sa.Column('incorrect_password_attempts', sa.Integer(), server_default='0', nullable=False))
    ### end Alembic commands ###


def downgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'incorrect_password_attempts')
    ### end Alembic commands ###


def upgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###

def upgrade_staging():
    pass

def downgrade_staging():
    pass