"""Add carga_trabajo table

Revision ID: 82232e902b20
Revises: e9d009ce36eb
Create Date: 2024-11-19 07:01:57.443283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82232e902b20'
down_revision = 'e9d009ce36eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carga_trabajo',
    sa.Column('id_carga', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_centro_trabajo', sa.Integer(), nullable=False),
    sa.Column('cantidad_horas_requeridas', sa.Float(), nullable=False),
    sa.Column('disponibilidad_recursos', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_centro_trabajo'], ['centros_trabajo.id_centro_trabajo'], ),
    sa.PrimaryKeyConstraint('id_carga')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carga_trabajo')
    # ### end Alembic commands ###
