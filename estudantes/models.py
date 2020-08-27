"""Modelo de Dados de Estudantes"""

from . import db

class Estudante(db.Model):
    __tablename__ = 'Estudantes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(70), index=False, unique=False, nullable=False)
    pai = db.Column(db.String(70), index=False, unique=False, nullable=True)
    mae = db.Column(db.String(70), index=False, unique=False, nullable=False)
    dt_nasc = db.Column(db.Datetime, index=False, unique=False, nullable=False)
    cpf = db.Column(db.Integer, index=False, unique=False, nullable=False)
    doc_id = db.Column(db.Integer, index=False, unique=False, nullable=True)
    org_exp_doc_id = db.Column(db.String(20), index=False, unique=False, nullable=True)
    dt_exp_doc_id = db.Column(db.Date, index=False, unique=False, nullable=True)

