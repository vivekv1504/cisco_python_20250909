from .models import Account
from .db import db
from .exceptions import NotFoundError, DuplicateError

def create_account(name, number, balance):
    if Account.query.filter_by(number=number).first():
        raise DuplicateError(f"Account with number {number} already exists.")
    account = Account(name=name, number=number, balance=balance)
    db.session.add(account)
    db.session.commit()
    return account

def get_account(account_id):
    account = Account.query.get(account_id)
    if not account:
        raise NotFoundError(f"Account {account_id} not found.")
    return account

def update_account(account_id, **kwargs):
    account = get_account(account_id)
    for key, value in kwargs.items():
        setattr(account, key, value)
    db.session.commit()
    return account

def delete_account(account_id):
    account = get_account(account_id)
    db.session.delete(account)
    db.session.commit()
