"""Adiciona colunas de controle de baixa das contas

Revision ID: 4d749f38372d
Revises: 163814092cef
Create Date: 2023-09-04 10:31:18.282245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d749f38372d'
down_revision = '163814092cef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contas_pagar_e_receber', sa.Column('data_baixa', sa.DateTime(), nullable=True))
    op.add_column('contas_pagar_e_receber', sa.Column('valor_baixa', sa.Numeric(), nullable=True))
    op.add_column('contas_pagar_e_receber', sa.Column('baixado', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contas_pagar_e_receber', 'baixado')
    op.drop_column('contas_pagar_e_receber', 'valor_baixa')
    op.drop_column('contas_pagar_e_receber', 'data_baixa')
    # ### end Alembic commands ###