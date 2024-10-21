import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'env_vars', '.env')
load_dotenv(env_path)

database = SQLAlchemy()


def initialize_extensions(app):
    database.init_app(app)


def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(__name__)

    app.config.from_object(config_type)

    initialize_extensions(app)

    return app



