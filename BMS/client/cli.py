import requests
import click

API_URL = 'http://localhost:5000'

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt=True)
@click.option('--number', prompt=True)
@click.option('--balance', default=0.0, type=float)
def create(name, number, balance):
    data = {'name': name, 'number': number, 'balance': balance}
    resp = requests.post(f"{API_URL}/accounts", json=data)
    click.echo(resp.json())

@cli.command()
@click.argument('account_id', type=int)
def get(account_id):
    resp = requests.get(f"{API_URL}/accounts/{account_id}")
    click.echo(resp.json())

@cli.command()
def list():
    resp = requests.get(f"{API_URL}/accounts")
    click.echo(resp.json())

if __name__ == '__main__':
    cli()
