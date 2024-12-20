"""Add materiales table

Revision ID: f3b501476530
Revises: 96cba2ba1d58
Create Date: 2024-11-19 06:02:25.185189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3b501476530'
down_revision = '96cba2ba1d58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('materiales',
    sa.Column('id_material', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre_material', sa.String(length=128), nullable=False),
    sa.Column('cantidad_necesaria', sa.Integer(), nullable=False),
    sa.Column('tiempo_entrega', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_material')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('materiales')
    # ### end Alembic commands ###
