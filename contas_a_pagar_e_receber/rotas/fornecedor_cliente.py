from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from contas_a_pagar_e_receber.schemas.fornecedor_cliente import ResponseFornecedorCliente, RequestFornecedorCliente
from contas_a_pagar_e_receber.modulos.fornecedor_cliente import (listar_fornecedor_cliente,
                                                                inserir_fornecedor_cliente,
                                                                get_fornecedor_cliente_por_id,
                                                                atualizar_fornecedor_cliente,
                                                                remover_fornecedor_cliente)
from contas_a_pagar_e_receber.servicos.database import get_db

rota = APIRouter()


@rota.post('/inserir_fornecedor_cliente', response_model=ResponseFornecedorCliente, status_code=status.HTTP_201_CREATED)
def criar_fornecedor_cliente(cliente: RequestFornecedorCliente, db: Session = Depends(get_db)):
    return inserir_fornecedor_cliente(cliente.dict(), db)


@rota.get('/listar_fornecedor_cliente', response_model=List[ResponseFornecedorCliente], status_code=status.HTTP_200_OK)
def lista_fornecedor_cliente(db: Session = Depends(get_db)):
    return listar_fornecedor_cliente(db)

@rota.get('/fornecedor_cliente/{id}', response_model=ResponseFornecedorCliente, status_code=status.HTTP_200_OK)
def cliente_fornecedor_id(id: int, db: Session = Depends(get_db)):
    return get_fornecedor_cliente_por_id(id, db)


@rota.put('/atualizar_fornecedor_cliente/{id}', response_model=ResponseFornecedorCliente, status_code=status.HTTP_200_OK)
def atualizar_cliente_fornecedor(id: int, fornecedor: RequestFornecedorCliente, db: Session = Depends(get_db)):
    return atualizar_fornecedor_cliente(id, fornecedor.dict(), db)


@rota.delete('/excluir_fornecedor_cliente/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remover_cliente_fornecedor(id: int, db: Session = Depends(get_db)):
    return remover_fornecedor_cliente(id, db)