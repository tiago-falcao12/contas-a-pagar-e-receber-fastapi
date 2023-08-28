from loguru import logger
from sqlalchemy.orm import Session

from contas_a_pagar_e_receber.modelos_db.contas import ContaPagarReceber


def inserir_contas_a_pagar_e_receber(conta: dict, db: Session) -> dict:
    logger.info(f"[+] REQUISITOU INSERIR CONTAS - ENTRADA: {conta}")
    conta_pagar_e_receber = ContaPagarReceber(**conta)
    db.add(conta_pagar_e_receber)
    db.commit()
    db.refresh(conta_pagar_e_receber)
    logger.info(
        f"[+] FINALIZOU INSERIR CONTAS - SAÍDA: {conta_pagar_e_receber.__dict__}")
    return conta_pagar_e_receber


def capturar_contas_a_pagar_e_receber(db: Session):
    logger.info(f"[+] REQUISITOU BUSCAR CONTAS A PAGAR E RECEBER")
    contas = db.query(ContaPagarReceber).all()
    logger.debug(contas)
    logger.info(f"[+] FINALIZOU BUSCAR CONTAS A PAGAR E RECEBER")
    return contas


def capturar_conta_a_pagar_e_receber(id: int, db: Session):
    conta = db.query(ContaPagarReceber).get(id)
    db.commit()
    db.refresh(conta)
    return conta


def atualizar_contas_a_receber_e_pagar(conta: dict(), id: int, db: Session):
    conta_pagar_e_receber = db.query(ContaPagarReceber).get(id)
    conta_pagar_e_receber.descricao = conta.get('descricao')
    conta_pagar_e_receber.tipo = conta.get('tipo')
    conta_pagar_e_receber.valor = conta.get('valor')

    db.add(conta_pagar_e_receber)
    db.commit()
    db.refresh(conta_pagar_e_receber)
    return conta_pagar_e_receber


def remover_contas_a_pagar_e_receber(id: int, db: Session):
    conta = db.query(ContaPagarReceber).get(id)
    db.delete(conta)
    db.commit()
