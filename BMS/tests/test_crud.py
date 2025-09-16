import pytest
from app import create_app, db
from app.models import Account

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as c:
        with app.app_context():
            db.create_all()
        yield c

def test_create_and_get_account(client):
    resp = client.post('/accounts', json={'name': 'Test', 'number': '123', 'balance': 100.0})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['name'] == 'Test'
    resp2 = client.get(f"/accounts/{data['id']}")
    assert resp2.status_code == 200
