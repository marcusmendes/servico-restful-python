"""
Classe que representa um endereço de uma pessoa e a tabela enderecos no banco de dados
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base


class Endereco(Base):
    __tablename__ = 'enderecos'
    id = Column(Integer, primary_key=True)
    pessoa_id = Column(Integer, ForeignKey("pessoa.id"))
    logradouro = Column(String, nullable=False)
    numero = Column(Integer, nullable=False)
    complemento = Column(String, nullable=True)

    # Método construtor
    def __init__(self, cep="", logradouro="", numero=0, complemento=""):
        self._cep = cep
        self._logradouro = logradouro
        self._numero = numero
        self._complemento = complemento

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep: str):
        self._cep = cep

    @property
    def logradouro(self):
        return self._logradouro

    @logradouro.setter
    def logradouro(self, logradouro: str):
        self._logradouro = logradouro

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero: int):
        self._numero = numero

    @property
    def complemento(self):
        return self._complemento

    @complemento.setter
    def complemento(self, complemento: str):
        self._complemento = complemento
