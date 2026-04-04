from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'Message': 'olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def teste_age_deve_retornar_idade():
    client = TestClient(app)

    response = client.get('/age')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Minha idade é 21</h1>' in response.text
