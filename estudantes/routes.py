"""Endpoints da aplicação"""

from datetime import datetime as dt
from flask import request, render_template, make_response, redirect, url_for
from flask import current_app as app
from .models import db, Estudante

@app.route('/', methods=['GET'])
def local_index():
    """root local da aplicação"""

    return render_template('')

@app.route('/inserir', methods=[ 'POST'])
def inserir():
    nome = request.form.get('nome')
    pai = request.form.get('pai')
    mae = request.form.get('mae')
    nasc = request.form.get('data_nacimento')
    cpf = request.form.get('cpf')
    doc_id = request.form.get('documento_identidade')
    orgao_expedidor = request.form.get('orgao_expedidor')
    data_expiracao = request.form.get('data_expiracao')

    if nome and mae:
        cadastrado = Estudante.query.filter(Estudante.nome == nome and Estudante.mae == mae).first()
        if not cadastrado:
            novo_estudante = Estudante(nome=nome, pai=pai,mae=mae, dt_nasc=data_from_str(nasc),
                                       cpf=int(cpf), doc_id=int(doc_id),
                                       org_exp_doc_id=orgao_expedidor,
                                       dt_exp_doc_id=data_from_str(data_expiracao))
            db.session.add(novo_estudante)
            db.session.commit()
        redirect(url_for('local_index'))


@app.route('/listar_todos', methods=[ 'GET'])
def listar():
    estudantes = Estudante.query.all()
    return render_template('', estudantes)


@app.route('/alterar/<int:id>', methods=['PUT'])
def alterar(id):
    if isinstance(id, int):
        estudante = Estudante.query.filter(Estudante.id == id).first()
        if estudante:
            nome = request.form.get('nome')
            nome = request.form.get('pai')
            nome = request.form.get('mae')
            nome = request.form.get('data_nascimento')
            nome = request.form.get('cpf')
            nome = request.form.get('documento_identidade')
            nome = request.form.get('orgao_expedidor')
            nome = request.form.get('data_expiracao')



def data_from_str(string):
    return dt.strptime(string,"%d/%m/%Y")