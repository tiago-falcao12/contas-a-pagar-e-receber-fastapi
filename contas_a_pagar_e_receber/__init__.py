from fastapi import FastAPI

from contas_a_pagar_e_receber.rotas import hello


app = FastAPI(title="Contas a Pagar e Receber",
              description="Um projeto simples com o uso do FastAPI",
              version="0.0.1")


app.include_router(hello.rota, prefix="/api", tags=["HELLO"])
