import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Tâche test'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Tâche test'
