from unittest.mock import patch
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from tests.client_test import get_client_test

client_count = get_client_test()


@patch("contas_a_pagar_e_receber.servicos.database.engine", return_value=create_engine)
@patch("contas_a_pagar_e_receber.servicos.database.SessionLocal", return_value=sessionmaker)
@patch("contas_a_pagar_e_receber.servicos.database.Base", return_value=declarative_base)
def test_get_contas_a_pagar_e_receber_200(*_):
    response = client_count.get('/api/contas')

    assert response.status_code == 200
