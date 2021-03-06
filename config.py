import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """General Configuration"""
    FLASK_ENV = os.environ.get("FLASK_ENV")

    """SQLAlchemy"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or 'sqlite:///' + os.path.join(basedir,
                                                                                                       'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") or False

    """Encryption"""
    SECRET_KEY = os.environ.get("SECRET_KEY")
