from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from flaskr.database import Base


class Pais(Base):
    __tablename__ = 'paises'
    id = Column(Integer, primary_key=True)
    sigla = Column(String, nullable=False)
    nome = Column(String, nullable=False)

    # Método construtor
    def __init__(self, id=0, sigla=None, nome=None):
        self.id = id
        self.sigla = sigla
        self.nome = nome


class Estado(Base):
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True)
    sigla = Column(String, nullable=False)
    nome = Column(String, nullable=False)

    # Método construtor
    def __init__(self, id=0, sigla=None, nome=None):
        self.id = id
        self.sigla = sigla
        self.nome = nome


class Cidade(Base):
    __tablename__ = 'cidades'
    id = Column(Integer, primary_key=True)
    sigla = Column(String, nullable=False)
    nome = Column(String, nullable=False)

    # Método construtor
    def __init__(self, id=0, sigla=None, nome=None):
        self.id = id
        self.sigla = sigla
        self.nome = nome


class Endereco(Base):
    __tablename__ = 'enderecos'
    id = Column(Integer, primary_key=True)
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"))
    logradouro = Column(String, nullable=False)
    numero = Column(Integer, nullable=False)
    complemento = Column(String, nullable=True)
    cidade_id = Column(Integer, ForeignKey("cidades.id"))
    cidade = relationship("Cidade", backref="enderecos")
    estado_id = Column(Integer, ForeignKey("estados.id"))
    estado = relationship("Estado", backref="enderecos")
    pais_id = Column(Integer, ForeignKey("paises.id"))
    pais = relationship("Pais", backref="enderecos")

    def __init__(self, cep=None, logradouro=None, numero=0,
                 complemento=None, cidade: Cidade = None, estado: Estado = None, pais: Pais = None):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.pais = pais


class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    endereco = relationship("Endereco", uselist=False, backref=backref("pessoas", lazy=True))

    def __init__(self, nome=None, cpf=None, data_nascimento=None, endereco: Endereco = None):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco