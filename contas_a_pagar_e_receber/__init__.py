from fastapi import FastAPI

from contas_a_pagar_e_receber.rotas import hello
from contas_a_pagar_e_receber.servicos.database import Base, engine
from contas_a_pagar_e_receber.modelos.contas import ContaPagarReceber


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Contas a Pagar e Receber",
              description="Um projeto simples com o uso do FastAPI",
              version="0.0.1")


app.include_router(hello.rota, prefix="/api", tags=["HELLO"])
