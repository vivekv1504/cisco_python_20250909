from flask import Flask
from .config import Config
from .db import db
from .logger import configure_logging
from .routes import register_routes
from .exceptions import register_error_handlers
from .extensions import mail  # import mail here

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    configure_logging(app)
    db.init_app(app)
    mail.init_app(app)

    register_routes(app)
    register_error_handlers(app)

    with app.app_context():
        db.create_all()

    return app
