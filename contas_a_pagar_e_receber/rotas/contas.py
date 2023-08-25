from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, status


from contas_a_pagar_e_receber.schemas.contas import ContasRequest, ContasResponse
from contas_a_pagar_e_receber.modulos.contas import inserir_contas_a_pagar_e_receber, capturar_contas_a_pagar_e_receber
from contas_a_pagar_e_receber.servicos.database import get_db

rota = APIRouter()


@rota.post("/inserir_contas", response_model=ContasResponse, status_code=status.HTTP_201_CREATED)
def inserindo_contas_a_pagar_e_receber(conta: ContasRequest, db: Session = Depends(get_db)):
    return inserir_contas_a_pagar_e_receber(conta.dict(), db)


@rota.get("/contas", status_code=status.HTTP_200_OK)
def capturar_contas(db: Session = Depends(get_db)):
    return capturar_contas_a_pagar_e_receber(db)
