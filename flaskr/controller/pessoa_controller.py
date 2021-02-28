from flask import Blueprint, request
from flaskr.service import pessoa_service

pessoas_blueprint = Blueprint('pessoas', __name__, url_prefix='/pessoas')


@pessoas_blueprint.route('/', methods=['POST'])
def criar_pessoa():
    return pessoa_service.criar_pessoa(request)


@pessoas_blueprint.route('/cpf/<string:cpf>', methods=['GET'])
def obter_pessoa_pelo_cpf(cpf):
    return pessoa_service.obter_pessoa_pelo_cpf(cpf)
