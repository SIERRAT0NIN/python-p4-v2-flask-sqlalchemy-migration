"""rename department

Revision ID: beccd8ff3e3f
Revises: a969f43b43a5
Create Date: 2023-11-13 16:26:41.152125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beccd8ff3e3f'
down_revision = 'a969f43b43a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('departments',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('name', sa.String(), nullable=False),
    # sa.Column('address', sa.String(), nullable=True),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.drop_table('department')
    # ### end Alembic commands ###
    op.rename_table('department','departments')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('department',
    # sa.Column('id', sa.INTEGER(), nullable=False),
    # sa.Column('name', sa.VARCHAR(), nullable=False),
    # sa.Column('address', sa.VARCHAR(), nullable=True),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.drop_table('departments')
    # ### end Alembic commands ###
    op.rename_table('departments', 'department')
