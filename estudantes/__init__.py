"""Flask boostrap"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

user = 'seu_usuario'
password = 'password'

db = SQLAlchemy()


def create():
    """Bootstrap modulo de estudantes"""
    app = Flask(__name__, instance_relative_config=False)

    app.config.update(
        FLASK_ENV="development",
        DEBUG=True,
        SECRET_KEY="Segredo",
        SQLALCHEMY_DATABASE_URI=f"sqlite:////tmp/escola.db",
        SQLALCHEMY_ECHO=False,
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

        return app
