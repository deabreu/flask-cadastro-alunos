"""Endpoints da aplicação"""

from datetime import datetime as dt
from flask import request, render_template, make_response, redirect, url_for
from flask import current_app as app
from .models import db, Estudante

@app.route('/', methods=['GET'])
def local_index():
    """root local da aplicação"""

    return render_template('')


@app.route('/tela_inserir', methods=['GET'])
def tela_inserir():
    return render_template('tela_inserir.html')


@app.route('/inserir', methods=['POST'])
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
    estudantes = Estudante.query.limit(1000).all() # limitador de segurança
    return render_template('', estudantes)


@app.route('/tela_alterar', methods=['GET'])
def tela_alterar():
    return render_template('tela_alterar.html')


@app.route('/alterar/<int:id>', methods=['PUT'])
def alterar(id):
    if isinstance(id, int):
        estudante = Estudante.query.filter(Estudante.id == id).first()
        if estudante:
            nome = request.form.get('nome')
            pai = request.form.get('pai')
            mae = request.form.get('mae')
            nasc = request.form.get('data_nascimento')
            cpf = request.form.get('cpf')
            doc_id = request.form.get('documento_identidade')
            orgao_expedidor = request.form.get('orgao_expedidor')
            data_expiracao = request.form.get('data_expiracao')
            estudante.nome = nome
            estudante.pai = pai
            estudante.mae = mae
            estudante.dt_nasc = data_from_str(nasc)
            estudante.cpf = cpf
            estudante.doc_id = int(doc_id)
            estudante.org_exp_doc_id = orgao_expedidor
            estudante.dt_exp_doc_id = data_from_str(data_expiracao)
    redirect(url_for('local_index'))


@app.route('/tela_remover', methods=['GET'])
def tela_remover():
    return render_template('tela_remover.html')


@app.route('/remover/<int:id>', methods=['DELETE'])
def remover(id):
    if isinstance(id, int):
        estudante = Estudante.query.filter(Estudante.id == id).first()
        if estudante:
            db.session.delete(estudante)
            db.commit()
    redirect(url_for('local_index'))


def data_from_str(string):
    return dt.strptime(string,"%d/%m/%Y")
