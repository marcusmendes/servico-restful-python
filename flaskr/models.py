from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import relationship, backref
from flaskr.database import Base

class CommonFields(object):
    id = Column(Integer, primary_key=True, autoincrement=True)
    sigla = Column(String, nullable=False)
    nome = Column(String, nullable=False)

    def __init__(self):
        pass

    def to_dict(self):
        return {
            "id": self.id,
            "sigla": self.sigla,
            "nome": self.nome
        }

class Pais(Base, CommonFields):
    __tablename__ = 'paises'

    # Método construtor
    def __init__(self, id=0, sigla=None, nome=None):
        self.id = id
        self.sigla = sigla
        self.nome = nome


class Estado(Base, CommonFields):
    __tablename__ = 'estados'

    # Método construtor
    def __init__(self, id=0, sigla=None, nome=None):
        self.id = id
        self.sigla = sigla
        self.nome = nome

class Cidade(Base, CommonFields):
    __tablename__ = 'cidades'

    # Método construtor
    def __init__(self, id=0, sigla=None, nome=None):
        self.id = id
        self.sigla = sigla
        self.nome = nome

class Endereco(Base):
    __tablename__ = 'enderecos'
    id = Column(Integer, primary_key=True)
    logradouro = Column(String, nullable=False)
    cep = Column(String, nullable=False)
    numero = Column(Integer, nullable=False)
    complemento = Column(String, nullable=True)
    cidade_id = Column(Integer, ForeignKey("cidades.id"))
    cidade = relationship("Cidade", backref="enderecos")
    estado_id = Column(Integer, ForeignKey("estados.id"))
    estado = relationship("Estado", backref="enderecos")
    pais_id = Column(Integer, ForeignKey("paises.id"))
    pais = relationship("Pais", backref="enderecos")
    __table_args__ = (UniqueConstraint('cep', 'numero', name='_cep_numero_uc'),)

    def __init__(self, cep=None, logradouro=None, numero=0,
                 complemento=None, cidade: Cidade = None, estado: Estado = None, pais: Pais = None):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def to_dict (self):
        json = {
            "id": self.id,
            "cep": self.cep,
            "logradouro": self.logradouro,
            "numero": self.numero,
            "cidade": self.cidade.to_dict(),
            "estado": self.estado.to_dict(),
            "pais": self.pais.to_dict()
        }

        if self.complemento:
            json["complemento"] = self.complemento
        
        return json


class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    endereco_id = Column(Integer, ForeignKey("enderecos.id"))
    endereco = relationship("Endereco", backref="pessoas")
    __table_args__ = (UniqueConstraint("cpf"),)

    def __init__(self, nome=None, cpf=None, data_nascimento=None, endereco: Endereco = None):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'endereco': self.endereco.to_dict ()
        }