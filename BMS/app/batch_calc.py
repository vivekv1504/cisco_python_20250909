from concurrent.futures import ThreadPoolExecutor
from .models import Account
from .db import db
from flask import current_app
import asyncio
from .models import Account

async def async_batch_total(accounts):
    await asyncio.sleep(0)  # Example placeholder for real async work
    return sum(acc.balance for acc in accounts)

async def batch_total_balances_async(batch_size=10):
    accounts = Account.query.all()
    batches = [accounts[i:i+batch_size] for i in range(0, len(accounts), batch_size)]
    tasks = [async_batch_total(batch) for batch in batches]
    return await asyncio.gather(*tasks)

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
