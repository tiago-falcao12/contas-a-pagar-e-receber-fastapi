from sqlalchemy import Column, Integer, Numeric, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from contas_a_pagar_e_receber.servicos.database import Base


class ContaPagarReceber(Base):
    __tablename__ = "contas_pagar_e_receber"

    id = Column(Integer, primary_key=True, autoincrement=True)

    descricao = Column(String(50))
    valor = Column(Numeric)
    tipo = Column(String(50))
    data_baixa = Column(DateTime())
    valor_baixa = Column(Numeric)
    baixado = Column(Boolean, default=False)

    fornecedor_cliente_id = Column(Integer, ForeignKey("fornecedor_cliente.id"))
    fornecedor = relationship("ForncedorCliente")