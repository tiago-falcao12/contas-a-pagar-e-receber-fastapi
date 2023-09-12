from fastapi import FastAPI

from contas_a_pagar_e_receber.rotas import hello, contas, fornecedor_cliente
from contas_a_pagar_e_receber.schemas.exceptions import NotFound, MyException
from contas_a_pagar_e_receber.modulos.exceptions import not_found_exception_handler, my_exception_exception_handler

# from contas_a_pagar_e_receber.servicos.database import Base, engine
# from contas_a_pagar_e_receber.modelos_db.contas import ContaPagarReceber


# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="Contas a Pagar e Receber",
              description="Um projeto simples com o uso do FastAPI",
              version="0.0.1")


app.add_exception_handler(NotFound, not_found_exception_handler)
app.add_exception_handler(MyException, my_exception_exception_handler)

app.include_router(hello.rota, tags=["HELLO"])
app.include_router(contas.rota, prefix="/api", tags=["CONTAS"])
app.include_router(fornecedor_cliente.rota, prefix="/api", tags=["FORNECEDORES"])
