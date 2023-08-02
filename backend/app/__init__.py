from flask import Flask, redirect
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from .models.database import db
from .models.user_model import security, user_datastore
from .router import api
from backend.config import Config

bcrypt = Bcrypt()


def register_extensions(app):
    db.init_app(app)
    security.init_app(app, user_datastore)
    bcrypt.init_app(app)
    api.init_app(app)


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
    configure_database(app)
    register_extensions(app)

    return app
