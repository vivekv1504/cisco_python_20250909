from flask import jsonify
from werkzeug.exceptions import NotFound
from flask import current_app as app

class NotFoundError(Exception):
    pass

class DuplicateError(Exception):
    pass

def register_error_handlers(app):
    @app.errorhandler(NotFound)
    def handle_not_found(e):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(NotFoundError)
    def handle_custom_not_found(e):
        return jsonify({'error': str(e)}), 404

    @app.errorhandler(DuplicateError)
    def handle_duplicate(e):
        return jsonify({'error': str(e)}), 409

    @app.errorhandler(Exception)
    def handle_generic(e):
        app.logger.error(f"Unhandled exception: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
