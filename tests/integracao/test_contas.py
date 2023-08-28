from tests.client_test import get_client_test
from tests.db_mock import create_db_test

client_account = get_client_test()


def test_get_contas_a_pagar_e_receber_200():
    create_db_test()

    response = client_account.get('/api/contas')

    assert response.status_code == 200
    assert response.json() == []


def test_get_id_conta_a_pagar_e_receber_200():
    create_db_test()

    conta = {
        "descricao": "Academia",
        "valor": 110,
        "tipo": "PAGAR"
    }

    response = client_account.post('/api/inserir_contas', json=conta)

    id = response.json()['id']

    conta['id'] = id

    response_get = client_account.get(f'/api/contas/{id}')
    assert response_get.status_code == 200
    assert response_get.json() == conta


def test_contas_a_pagar_e_receber_422():
    json = {
        "descricao": "123456789123456789123456789123456789123456789123456789123456789",
        "valor": 0,
        "tipo": "PAGAR"
    }

    response = client_account.post('/api/inserir_contas', json=json)
    assert response.status_code == 422


def test_insert_conta_a_pagar_e_receber_201():
    create_db_test()

    conta = {
        "descricao": "Academia",
        "valor": 110,
        "tipo": "PAGAR"
    }

    response = client_account.post('/api/inserir_contas', json=conta)

    conta["id"] = 1

    assert response.status_code == 201
    assert response.json() == conta


def test_update_conta_a_pagar_e_receber():
    create_db_test()

    conta_inserir = {
        "descricao": "Academia",
        "valor": 110,
        "tipo": "PAGAR"
    }

    response = client_account.post('/api/inserir_contas', json=conta_inserir)

    id = response.json()['id']

    conta_atualizar = {
        "descricao": "Academia",
        "valor": 100,
        "tipo": "PAGAR"
    }

    response_put = client_account.put(
        f'/api/atualizar_contas/{id}', json=conta_atualizar)

    assert response_put.status_code == 200
    assert response_put.json()['valor'] == 100


def test_delete_conta_a_pagar_e_receber():
    create_db_test()

    conta_inserir = {
        "descricao": "Academia",
        "valor": 110,
        "tipo": "PAGAR"
    }

    response = client_account.post('/api/inserir_contas', json=conta_inserir)

    id = response.json()['id']

    response_del = client_account.delete(f'/api/remover_contas/{id}')

    assert response_del.status_code == 204
