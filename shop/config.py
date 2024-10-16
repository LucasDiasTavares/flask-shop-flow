import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_ENV = os.getenv("FLASK_ENV")
    DEBUG = os.getenv("DEBUG")
    CONFIG_TYPE = os.getenv("CONFIG_TYPE")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    FLASK_DEBUG = False
    FLASK_ENV = 'production'
