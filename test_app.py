import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    res = client.get('/')
    assert res.status_code == 200

def test_predict_route(client):
    res = client.post('/predict', data={'feature1': 5})
    assert res.status_code == 200
    assert b'Price of House will be Rs.' in res.data
