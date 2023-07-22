from flask import Flask, redirect, url_for
from flask_cors import CORS

from .models.database import db
from .models.user_model import security, user_datastore
from backend.config import Config


def register_extensions(app):
    db.init_app(app)
    security.init_app(app, user_datastore)


def configure_database(app):
    @app.before_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, origins="http://localhost:5173")
    register_extensions(app)
    configure_database(app)

    return app
