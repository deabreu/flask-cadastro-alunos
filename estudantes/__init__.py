"""Flask boostrap"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create():
    """Bootstrap modulo de estudantes"""
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

        return app
