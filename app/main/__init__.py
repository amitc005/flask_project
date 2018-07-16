from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name



db = SQLAlchemy()

def page_not_found(e):
  return "<H1>Link is Broken</H1>", 404

def server_error(e):
  return "<H1>Server Error</H1>", 500

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, server_error)
    db.init_app(app)

    return app
