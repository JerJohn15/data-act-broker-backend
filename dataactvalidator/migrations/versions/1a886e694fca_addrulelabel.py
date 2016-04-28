"""addRuleLabel

Revision ID: 1a886e694fca
Revises: 0b730d69f9bd
Create Date: 2016-03-28 09:43:59.152000

"""

# revision identifiers, used by Alembic.
revision = '1a886e694fca'
down_revision = '0b730d69f9bd'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rule', sa.Column('rule_label', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rule', 'rule_label')
    ### end Alembic commands ###