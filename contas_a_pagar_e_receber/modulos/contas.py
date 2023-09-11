from datetime import datetime

from loguru import logger
from sqlalchemy.orm import Session
from sqlalchemy import extract

from contas_a_pagar_e_receber.modulos.exceptions import NotFound, MyException
from contas_a_pagar_e_receber.config import QT_MAX_REGISTROS_MES
from contas_a_pagar_e_receber.modelos_db.contas import ContaPagarReceber
from contas_a_pagar_e_receber.modulos.fornecedor_cliente import get_fornecedor_cliente_por_id


def inserir_contas_a_pagar_e_receber(conta: dict, db: Session) -> dict:
    logger.info(f"[+] REQUISITOU INSERIR CONTAS - ENTRADA: {conta}")
    verificar_fornecedor_cliente(conta, db)
    verifica_e_valida_quantidade_de_registros_por_mes_e_ano(db, conta['data_previsao'])
    
    conta_pagar_e_receber = ContaPagarReceber(**conta)
    db.add(conta_pagar_e_receber)
    db.commit()
    db.refresh(conta_pagar_e_receber)
    logger.info(
        f"[+] FINALIZOU INSERIR CONTAS - SAÍDA: {conta_pagar_e_receber.__dict__}")
    return conta_pagar_e_receber


def baixar_contas_a_pagar_e_receber(id: int, db: Session):
    conta = verificar_conta_por_id(id, db)

    if (conta.baixado and conta.valor_baixa != conta.valor) or not conta.baixado:

        conta.data_baixa = datetime.now()
        conta.valor_baixa = conta.valor
        conta.baixado = True        
        db.add(conta)
        db.commit()
        db.refresh(conta)       
    return conta


def capturar_contas_a_pagar_e_receber(db: Session):
    logger.info(f"[+] REQUISITOU BUSCAR CONTAS A PAGAR E RECEBER")
    contas = db.query(ContaPagarReceber).all()
    logger.debug(contas)
    logger.info(f"[+] FINALIZOU BUSCAR CONTAS A PAGAR E RECEBER")
    return contas


def capturar_conta_a_pagar_e_receber(id: int, db: Session):
    conta = verificar_conta_por_id(id, db)
    return conta


def atualizar_contas_a_receber_e_pagar(conta: dict(), id: int, db: Session):
    conta_pagar_e_receber = verificar_conta_por_id(id, db)
    verificar_fornecedor_cliente(conta, db)

    conta_pagar_e_receber.descricao = conta.get('descricao')
    conta_pagar_e_receber.tipo = conta.get('tipo')
    conta_pagar_e_receber.valor = conta.get('valor')
    conta_pagar_e_receber.fornecedor_cliente_id = conta.get(
        'fornecedor_cliente_id')

    db.add(conta_pagar_e_receber)
    db.commit()
    db.refresh(conta_pagar_e_receber)
    return conta_pagar_e_receber


def remover_contas_a_pagar_e_receber(id: int, db: Session):
    conta = verificar_conta_por_id(id, db)

    db.delete(conta)
    db.commit()


def verificar_conta_por_id(id: int, db: Session):
    conta = db.query(ContaPagarReceber).get(id)
    if conta is None:
        raise NotFound(name="Conta")
    return conta


def verificar_fornecedor_cliente(conta: dict, db: Session):
    id_fornecedor = conta.get('fornecedor_cliente_id')

    if id_fornecedor:
        get_fornecedor_cliente_por_id(id_fornecedor, db)

def verifica_e_valida_quantidade_de_registros_por_mes_e_ano(db: Session, data: str):
    mes, ano = data.month, data.year

    qtd_registros = db.query(ContaPagarReceber). \
                       filter(extract('month', ContaPagarReceber.data_previsao) == mes,
                              extract('year', ContaPagarReceber.data_previsao) == ano).count()

    if qtd_registros >= eval(QT_MAX_REGISTROS_MES):
        raise MyException(mensagem=" Oops! Você atingiu o limite máximo para inserir contas neste mês!", status=203)
