"""
Classe responsável por definir uma pessoa no serviço RESTful e representar a tabela pessoas no banco de dados
"""
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.database.base import Base
from app.model.endereco import Endereco


class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    endereco = relationship("Endereco", uselist=False, backref="pessoa")

    # Método construtor
    def __init__(self, nome="", cpf="", data_nascimento="", endereco: Endereco = ""):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._endereco = endereco

    # @property é usado no método GETTER que obtém o valor de um atributo
    @property
    def nome(self):
        return self._nome

    # @nome.setter é usado no método SETTER que seta o valor de um atributo
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self._cpf = cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str):
        self.data_nascimento = data_nascimento

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: Endereco):
        self._endereco = endereco
