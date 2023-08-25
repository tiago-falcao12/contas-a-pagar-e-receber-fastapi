from sqlalchemy import Column, Integer, Numeric, String

from contas_a_pagar_e_receber.servicos.database import Base


class ContaPagarReceber(Base):
    __tablename__ = "contas_pagar_e_receber"

    id = Column(Integer, primary_key=True, autoincrement=True)

    descricao = Column(String(50))
    valor = Column(Numeric)
    tipo = Column(String(50))
