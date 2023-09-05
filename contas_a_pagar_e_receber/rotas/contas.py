from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, status


from contas_a_pagar_e_receber.schemas.contas import ContasRequest, ContasReponseBaixa
from contas_a_pagar_e_receber.modulos.contas import (inserir_contas_a_pagar_e_receber,
                                                     capturar_contas_a_pagar_e_receber,
                                                     capturar_conta_a_pagar_e_receber,
                                                     atualizar_contas_a_receber_e_pagar,
                                                     remover_contas_a_pagar_e_receber,
                                                     baixar_contas_a_pagar_e_receber)
from contas_a_pagar_e_receber.servicos.database import get_db

rota = APIRouter()


@rota.post("/inserir_contas", response_model=ContasReponseBaixa, status_code=status.HTTP_201_CREATED)
def inserindo_contas_a_pagar_e_receber(conta: ContasRequest, db: Session = Depends(get_db)):
    return inserir_contas_a_pagar_e_receber(conta.dict(), db)


@rota.post("/baixar_contas/{identificador_conta}", response_model=ContasReponseBaixa, status_code=status.HTTP_201_CREATED)
def baixando_conta_a_pagar_e_receber(identificador_conta: int, db: Session = Depends(get_db)):
    return baixar_contas_a_pagar_e_receber(identificador_conta, db)

@rota.get("/contas", response_model=List[ContasReponseBaixa], status_code=status.HTTP_200_OK)
def listando_contas_a_pagar_e_receber(db: Session = Depends(get_db)):
    return capturar_contas_a_pagar_e_receber(db)


@rota.get("/contas/{identificador_conta}", response_model=ContasReponseBaixa, status_code=status.HTTP_200_OK)
def capturando_conta_a_pagar_e_receber(identificador_conta: int, db: Session = Depends(get_db)):
    return capturar_conta_a_pagar_e_receber(identificador_conta, db)


@rota.put("/atualizar_contas/{identificador_conta}", response_model=ContasReponseBaixa, status_code=status.HTTP_200_OK)
def atualizando_conta_a_pagar_e_receber(identificador_conta: int, conta: ContasRequest, db: Session = Depends(get_db)):
    return atualizar_contas_a_receber_e_pagar(conta.dict(), identificador_conta, db)


@rota.delete("/remover_contas/{identificador_conta}", status_code=status.HTTP_204_NO_CONTENT)
def excluindo_conta_a_pagar_e_receber(identificador_conta: int, db: Session = Depends(get_db)):
    return remover_contas_a_pagar_e_receber(identificador_conta, db)
