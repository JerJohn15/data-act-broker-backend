"""adding timestamps to all tables

Revision ID: c0a714ade734
Revises: 1a886e694fca
Create Date: 2016-04-20 14:46:06.407765

"""

# revision identifiers, used by Alembic.
revision = 'c0a714ade734'
down_revision = '1a886e694fca'
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
    op.add_column('field_type', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('field_type', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('file_columns', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('file_columns', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('file_type', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('file_type', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('multi_field_rule', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('multi_field_rule', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('multi_field_rule_type', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('multi_field_rule_type', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('rule', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('rule', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('rule_timing', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('rule_timing', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('rule_type', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('rule_type', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('tas_lookup', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('tas_lookup', sa.Column('updated_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tas_lookup', 'updated_at')
    op.drop_column('tas_lookup', 'created_at')
    op.drop_column('rule_type', 'updated_at')
    op.drop_column('rule_type', 'created_at')
    op.drop_column('rule_timing', 'updated_at')
    op.drop_column('rule_timing', 'created_at')
    op.drop_column('rule', 'updated_at')
    op.drop_column('rule', 'created_at')
    op.drop_column('multi_field_rule_type', 'updated_at')
    op.drop_column('multi_field_rule_type', 'created_at')
    op.drop_column('multi_field_rule', 'updated_at')
    op.drop_column('multi_field_rule', 'created_at')
    op.drop_column('file_type', 'updated_at')
    op.drop_column('file_type', 'created_at')
    op.drop_column('file_columns', 'updated_at')
    op.drop_column('file_columns', 'created_at')
    op.drop_column('field_type', 'updated_at')
    op.drop_column('field_type', 'created_at')
    ### end Alembic commands ###

def upgrade_error_data():
    pass

def downgrade_error_data():
    pass

def upgrade_job_tracker():
    pass

def downgrade_job_tracker():
    pass

def upgrade_user_manager():
    pass

def downgrade_user_manager():
    pass

def upgrade_staging():
    pass

def downgrade_staging():
    pass