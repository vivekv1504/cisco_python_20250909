from concurrent.futures import ThreadPoolExecutor
from .models import Account
from .db import db
from flask import current_app

def calc_batch_total(accounts):
    return sum(ac.balance for ac in accounts)

def batch_total_balances(batch_size=None):
    if batch_size is None:
        batch_size = current_app.config.get('BATCH_SIZE', 10)
    accounts = Account.query.all()
    batches = [accounts[i:i+batch_size] for i in range(0, len(accounts), batch_size)]
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(calc_batch_total, batches))
    return results
