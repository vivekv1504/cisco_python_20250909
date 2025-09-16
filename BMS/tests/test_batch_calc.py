import pytest
from app import create_app, db
from app.models import Account
from app.batch_calc import batch_total_balances

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        # Seed test accounts
        db.session.add_all([
            Account(name='A1', number='n1', balance=100),
            Account(name='A2', number='n2', balance=200),
            Account(name='A3', number='n3', balance=300),
        ])
        db.session.commit()
    return app

def test_batch_totals(app):
    with app.app_context():
        totals = batch_total_balances(batch_size=2)
        assert totals == [300, 300]  # 100+200, and 300 alone
