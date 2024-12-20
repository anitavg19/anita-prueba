"""Add calendario_capacidad table

Revision ID: b1951c1d40a3
Revises: 82232e902b20
Create Date: 2024-11-19 07:11:35.496377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1951c1d40a3'
down_revision = '82232e902b20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calendario_capacidad',
    sa.Column('id_calendario_capacidad', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('horas_laborables', sa.Float(), nullable=False),
    sa.Column('capacidad_restante', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id_calendario_capacidad')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calendario_capacidad')
    # ### end Alembic commands ###
