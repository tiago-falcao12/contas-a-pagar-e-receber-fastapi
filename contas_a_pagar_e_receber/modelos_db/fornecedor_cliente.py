from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from contas_a_pagar_e_receber.servicos.database import Base


class ForncedorCliente(Base):
    __tablename__ = "fornecedor_cliente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255))
