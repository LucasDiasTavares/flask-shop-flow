import os
from sqlalchemy.engine.url import URL


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_ENV = os.getenv("FLASK_ENV")
    DEBUG = os.getenv("DEBUG")
    CONFIG_TYPE = os.getenv("CONFIG_TYPE")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")


class DevelopmentConfig(Config):
    DEBUG = True
    url_obj = URL.create(
        "postgresql+psycopg2",
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME")
    )
    SQLALCHEMY_DATABASE_URI = url_obj


class ProductionConfig(Config):
    DEBUG = False
    FLASK_DEBUG = False
    FLASK_ENV = 'production'
