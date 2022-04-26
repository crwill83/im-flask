"""empty message

Revision ID: 800c760bb12b
Revises: 1eae9952030d
Create Date: 2022-03-13 20:37:59.933613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '800c760bb12b'
down_revision = '1eae9952030d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rental',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_rented', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('inventory_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['inventory_id'], ['inventory.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rental')
    # ### end Alembic commands ###