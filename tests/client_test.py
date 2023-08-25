from fastapi.testclient import TestClient
from contas_a_pagar_e_receber import app


def get_client_test():
    return TestClient(app)
