"""Configurações de bootstrap"""

class Config(object):
    """Flask configuration object"""
    FLASK_ENV = "development"
    DEBUG=True
    SECRET_KEY = "Segredo"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://seu_usuario:password@127.0.0.1:3306/Escola"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
