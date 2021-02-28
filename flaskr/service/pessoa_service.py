from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from flaskr.database import db_session
from flaskr.model.pessoa import Pessoa


def criar_pessoa(request):
    pass


def obter_pessoa_pelo_cpf(cpf: str):
    try:
        pessoa = db_session.query(Pessoa).filter(Pessoa.cpf == cpf).one()
        return pessoa
    except MultipleResultsFound:
        raise
    except NoResultFound:
        raise
