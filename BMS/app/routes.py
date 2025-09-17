"""routes.py - Flask Blueprint for Banking Management System 
API Routes"""
from flask import Blueprint, jsonify, request
from .crud import create_account, get_account, update_account, delete_account
from .emailer import notify_account_creation
from .batch_calc import batch_total_balances, asyncio
from flask import send_from_directory,current_app
from .models import Account

import os
bp = Blueprint('api', __name__)
"""the blueprint is designed to be registered in the Flask app factory via register_routes."""
@bp.route('/')
def index():
    return jsonify({'message': 'Welcome to Account API'}), 200
"""- GET / : Returns a welcome message for the Account API."""
@bp.route('/www.png')
def favicon():
    """GET /www.png : Serves the favicon image from the static directory."""
    static_folder = os.path.join(current_app.root_path, 'static')
    return send_from_directory(static_folder, 'www.png', mimetype='image/vnd.microsoft.icon')

@bp.route('/accounts', methods=['POST'])
def api_create_account():
    """POST /accounts : Creates a new bank account, triggers email notification."""
    data = request.json
    account = create_account(data['name'], data['number'], data.get('balance', 0.0))
    notify_account_creation(account)
    return jsonify({
        'id': account.id, 'name': account.name, 
        'number': account.number, 'balance': account.balance
    }), 201
@bp.route('/accounts', methods=['GET'])
def api_list_accounts():
    """ GET /accounts : Retrieves a list of all bank accounts with details."""
    accounts = Account.query.all()
    result = [{
        "id": acc.id,
        "name": acc.name,
        "number": acc.number,
        "balance": acc.balance,
        "error":100
    } for acc in accounts]
    return jsonify(result)

@bp.route('/accounts/<int:account_id>', methods=['GET'])
def api_get_account(account_id):
    """- GET /accounts/<account_id> : Retrieves the details of a specific account by ID."""
    account = get_account(account_id)
    return jsonify({
        'id': account.id, 'name': account.name,
        'number': account.number, 'balance': account.balance
    })

@bp.route('/accounts/<int:account_id>', methods=['PUT'])
def api_update_account(account_id):
    """PUT /accounts/<account_id> : Updates the specified account with new data."""
    data = request.json
    account = update_account(account_id, **data)
    return jsonify({
        'id': account.id, 'name': account.name,
        'number': account.number, 'balance': account.balance
    })

@bp.route('/accounts/<int:account_id>', methods=['DELETE'])
def api_delete_account(account_id):
    """DELETE /accounts/<account_id> : Deletes the specified account."""
    delete_account(account_id)
    return jsonify({'message': f'Account {account_id} deleted successfully.'}), 204

@bp.route('/accounts/batch-total', methods=['GET'])
def api_batch_total():
    batch_size = int(request.args.get('batch_size', 10))
    totals = batch_total_balances(batch_size)
    return jsonify({'batch_totals': totals})

def register_routes(app):
    app.register_blueprint(bp)
