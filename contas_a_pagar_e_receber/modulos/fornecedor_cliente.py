from sqlalchemy.orm import Session

from contas_a_pagar_e_receber.schemas.exceptions import NotFound

from contas_a_pagar_e_receber.modelos_db.fornecedor_cliente import ForncedorCliente

def listar_fornecedor_cliente(db: Session):
    cliente = db.query(ForncedorCliente).all()
    return cliente

def get_fornecedor_cliente_por_id(id: int, db: Session):
    cliente = verificar_id(id, db)
    return cliente

def inserir_fornecedor_cliente(cliente: dict, db: Session):
    fornecedor = ForncedorCliente(**cliente)
    db.add(fornecedor)
    db.commit()
    db.refresh(fornecedor)
    return fornecedor

def atualizar_fornecedor_cliente(id: int, fornecedor: dict, db: Session):
    cliente = verificar_id(id, db)
    cliente.nome = fornecedor.get("nome")
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def remover_fornecedor_cliente(id: int, db: Session):
    cliente = verificar_id(id, db)
    db.delete(cliente)
    db.commit()

def verificar_id(id: int, db: Session):
    encontrado = db.query(ForncedorCliente).get(id)

    if encontrado is None:
        raise NotFound(name="Fornecedor")
    return encontrado