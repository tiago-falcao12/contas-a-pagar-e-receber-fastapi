from fastapi.testclient import TestClient

from contas_a_pagar_e_receber.modulos.hello import hello_world
from tests.client_test import get_client_test


client = get_client_test()


def test_hello_deve_retornar_200_e_mensagem():

    response = client.get("/")
    retorno_hello_wolrd = hello_world()

    assert response.status_code == 200
    assert response.json() == retorno_hello_wolrd
