from fastapi.testclient import TestClient
from contas_a_pagar_e_receber import app
from contas_a_pagar_e_receber.modulos.hello import hello_world


client = TestClient(app)


def test_hello_deve_retornar_200_e_mensagem():

    response = client.get("/api/")
    retorno_hello_wolrd = hello_world()

    assert response.status_code == 200
    assert response.json() == retorno_hello_wolrd