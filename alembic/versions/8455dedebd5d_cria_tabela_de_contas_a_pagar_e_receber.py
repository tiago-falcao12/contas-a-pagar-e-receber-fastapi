"""Cria tabela de contas a pagar e receber

Revision ID: 8455dedebd5d
Revises: 
Create Date: 2023-08-25 11:04:58.026323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8455dedebd5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('contas_pagar_e_receber',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('descricao', sa.String(
                        length=50), nullable=True),
                    sa.Column('valor', sa.Numeric(), nullable=True),
                    sa.Column('tipo', sa.String(length=50), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('contas_pagar_e_receber')
