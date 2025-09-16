import logging
import json
from pythonjsonlogger import jsonlogger

def configure_logging(app):
    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config.get('LOG_LEVEL', 'INFO'))
