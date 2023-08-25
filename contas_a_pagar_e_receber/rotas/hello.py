from fastapi import APIRouter

from contas_a_pagar_e_receber.modulos.hello import hello_world
from contas_a_pagar_e_receber.modelos_db.hello import HelloResponse

rota = APIRouter()


@rota.get("/", response_model=HelloResponse, status_code=200)
def hello():
    return hello_world()
