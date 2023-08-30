from tests.client_test import get_client_test
from tests.db_mock import create_db_test

client = get_client_test()


def test_listar_fornecedor_cliente_vazio_200():
    create_db_test()

    response = client.get('/api/listar_fornecedor_cliente')
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_capturar_fornecedor_cliente_por_id_200():
    create_db_test()

    json_fornecedor = {"nome": "Tiago"}

    response = client.post('/api/inserir_fornecedor_cliente', json=json_fornecedor)
    id = response.json()['id']

    json_fornecedor['id'] = id

    response_get_id = client.get(f'/api/fornecedor_cliente/{id}')

    assert response_get_id.status_code == 200
    assert response_get_id.json() == json_fornecedor


def test_criar_fornecedor_cliente_200():
    create_db_test()

    nome = 'Tiago nunes da silva'
    fornecedor_inserir = {"nome": f"{nome}"}

    response = client.post('/api/inserir_fornecedor_cliente', json=fornecedor_inserir)

    assert response.status_code == 201
    assert response.json()['nome'] == nome

def test_atualizar_fornecedor_cliente_200():
    create_db_test()

    json_criar = {"nome": "Anna"}

    response = client.post('/api/inserir_fornecedor_cliente', json=json_criar)

    id = response.json()['id']

    json_atualizar = {"nome": "Tiago"}

    response_put = client.put(f'/api/atualizar_fornecedor_cliente/{id}', json=json_atualizar)
    assert response_put.status_code == 200
    assert response_put.json()['nome'] == "Tiago"


def test_excluir_fornecedor_cliente_204():
    create_db_test()

    response = client.post('/api/inserir_fornecedor_cliente', json={"nome": "tiago"})
    
    id = response.json()['id']

    response_delete = client.delete(f'/api/excluir_fornecedor_cliente/{id}')
    assert response_delete.status_code == 204
