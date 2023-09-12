from tests.client_test import get_client_test
from tests.db_mock import create_db_test
from contas_a_pagar_e_receber.config import QT_MAX_REGISTROS_MES


client_account = get_client_test()


def test_get_contas_a_pagar_e_receber_200():
    create_db_test()

    response = client_account.get('/api/contas')

    assert response.status_code == 200
    assert response.json() == []


def test_get_id_conta_a_pagar_e_receber_com_id_fornecedor_cliente_200():
    create_db_test()

    client_account.post('/api/inserir_fornecedor_cliente',
                        json={"nome": "BASA"})

    conta = {
        "descricao": "Academia",
        "valor": 110,
        "tipo": "PAGAR",
        "data_previsao": '2023-09-06',
        "fornecedor_cliente_id": 1
    }

    id_fornecedor = conta.get('fornecedor_cliente_id')

    response_fornecedor = client_account.get(
        f'/api/fornecedor_cliente/{id_fornecedor}')

    response = client_account.post('/api/inserir_contas', json=conta)

    id = response.json()['id']

    conta['id'] = id
    del conta['fornecedor_cliente_id']

    conta.update({"fornecedor": response_fornecedor.json()})
    conta['valor_baixa'] = None
    conta['data_baixa'] = None
    conta['baixado'] = False

    response_get = client_account.get(f'/api/contas/{id}')

    assert response_get.status_code == 200
    assert response_get.json() == conta


def test_contas_a_pagar_e_receber_422():
    json = {
        "descricao": "123456789" * 5,
        "valor": 0,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
    }

    response = client_account.post('/api/inserir_contas', json=json)
    assert response.status_code == 422


def test_insert_contas_a_pagar_e_receber_com_limite_de_registros():
    create_db_test()

    conta = {
        "descricao": "Academia",
        "valor": 110,
        "tipo": "PAGAR",
        "data_previsao": '2023-09-06'
    }

    for _ in range(eval(QT_MAX_REGISTROS_MES)):
        client_account.post('/api/inserir_contas', json=conta)
    

    response = client_account.post('/api/inserir_contas', json=conta)
    assert response.status_code == 203


def test_insert_conta_a_pagar_e_receber_com_id_cliente_fornecedor_201():
    create_db_test()

    client_account.post('/api/inserir_fornecedor_cliente',
                        json={"nome": "BASA"})

    conta = {
        "descricao": "Academia",
        "valor": 110,
        "tipo": "PAGAR",
        "data_previsao": '2023-09-06',
        "fornecedor_cliente_id": 1
    }

    id_fornecedor = conta.get('fornecedor_cliente_id')

    response_fornecedor = client_account.get(
        f'/api/fornecedor_cliente/{id_fornecedor}')

    response = client_account.post('/api/inserir_contas', json=conta)

    id = response.json()['id']

    conta['id'] = id
    del conta['fornecedor_cliente_id']

    conta.update({"fornecedor": response_fornecedor.json()})
    conta['valor_baixa'] = None
    conta['data_baixa'] = None
    conta['baixado'] = False

    assert response.status_code == 201
    assert response.json() == conta


def test_insert_conta_a_pagar_e_redeber_sem_id_cliente_fornecedor_201():
    create_db_test()

    conta = {
        "descricao": "Academia",
        "valor": 110,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
    }

    response = client_account.post('/api/inserir_contas', json=conta)

    conta["id"] = 1
    conta['fornecedor'] = None
    conta['valor_baixa'] = None
    conta['data_baixa'] = None
    conta['baixado'] = False

    assert response.status_code == 201
    assert response.json() == conta


def test_insert_conta_a_pagar_e_receber_com_id_fornecedor_cliente_inexistente_erro_404():
    create_db_test()

    conta = {
        "descricao": "Academia",
        "valor": 110,
        "tipo": "PAGAR",
        "data_previsao": '2023-09-06',
        "fornecedor_cliente_id": 1
    }

    response = client_account.post('/api/inserir_contas', json=conta)

    assert response.status_code == 404

def test_baixar_contas_a_pagar_receber_201():
    create_db_test()

    conta_inserir = {
        "descricao": "Academia",
        "valor": 110,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
        }

    client_account.post('/api/inserir_contas', json=conta_inserir)

    response = client_account.post("/api/baixar_contas/1")

    assert response.status_code == 201
    assert response.json()['baixado'] is True
    assert response.json()['valor_baixa'] == conta_inserir['valor']

def test_baixar_contas_a_pagar_e_receber_com_valor_alterado():
    create_db_test()
    conta_inserir = {
        "descricao": "Academia",
        "valor": 110,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
        }

    client_account.post('/api/inserir_contas', json=conta_inserir)
    client_account.post("/api/baixar_contas/1")

    conta_atualizar = {
        "descricao": "Academia",
        "valor": 200,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
    }

    client_account.put('/api/atualizar_contas/1', json=conta_atualizar)
    response = client_account.post("/api/baixar_contas/1")

    assert response.status_code == 201
    assert response.json()['valor_baixa'] == 200
    assert response.json()['baixado'] is True





def test_update_conta_a_pagar_e_receber():
    create_db_test()

    conta_inserir = {
        "descricao": "Academia",
        "valor": 110,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
    }

    response = client_account.post('/api/inserir_contas', json=conta_inserir)

    id = response.json()['id']

    conta_atualizar = {
        "descricao": "Academia",
        "valor": 100,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
    }

    response_put = client_account.put(
        f'/api/atualizar_contas/{id}', json=conta_atualizar)

    assert response_put.status_code == 200
    assert response_put.json()['valor'] == 100


def test_update_conta_a_pagar_e_receber_fornecedor_cliente_id():
    create_db_test()

    client_account.post('/api/inserir_fornecedor_cliente',
                        json={"nome": "BASA"})

    conta_inserir = {
        "descricao": "Academia",
        "valor": 110,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
    }

    response = client_account.post('/api/inserir_contas', json=conta_inserir)

    id = response.json()['id']

    conta_atualizar = {
        "descricao": "Academia",
        "valor": 100,
        "tipo": "PAGAR",
        "data_previsao": '2023-09-06',
        "fornecedor_cliente_id": 1
    }

    response_put = client_account.put(
        f'/api/atualizar_contas/{id}', json=conta_atualizar)

    assert response_put.status_code == 200
    assert response_put.json()['valor'] == 100
    assert response_put.json()['fornecedor']['nome'] == "BASA"


def test_delete_conta_a_pagar_e_receber():
    create_db_test()

    conta_inserir = {
        "descricao": "Academia",
        "valor": 110,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
    }

    response = client_account.post('/api/inserir_contas', json=conta_inserir)

    id = response.json()['id']

    response_del = client_account.delete(f'/api/remover_contas/{id}')

    assert response_del.status_code == 204


def test_capturar_contas_a_pagar_e_receber_404():
    create_db_test()

    response = client_account.get('/api/contas/3')
    assert response.status_code == 404


def test_atualizar_contas_a_pagar_e_receber_404():
    create_db_test()
    conta_atualizar = {
        "descricao": "Academia",
        "valor": 100,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
    }
    response = client_account.put(
        '/api/atualizar_contas/3', json=conta_atualizar)
    assert response.status_code == 404


def test_remover_contas_a_pagar_e_receber_404():
    create_db_test()

    response = client_account.delete('/api/remover_contas/3')
    assert response.status_code == 404

def test_total_previsao_contas_por_mes():
    create_db_test()

    conta_1 = {
        "descricao": "Academia",
        "valor": 100,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
    }

    conta_2 = {
        "descricao": "mercado",
        "valor": 900,
        "data_previsao": '2023-09-06',
        "tipo": "PAGAR"
    }

    client_account.post("/api/inserir_contas", json=conta_1)
    client_account.post("/api/inserir_contas", json=conta_2)

    response = client_account.get("/api/contas_total_mes", params={"ano": 2023})

    assert response.status_code == 200
    assert response.json()[0]['valor_total'] == 1000

