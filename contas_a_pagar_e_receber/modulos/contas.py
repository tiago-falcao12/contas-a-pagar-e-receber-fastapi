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
    contas = db.query(ContaPagarReceber).all()
    logger.debug(contas)
    return dict(resultado=contas)
