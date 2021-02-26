"""
Classe que representa um estado de um endereço de uma pessoa e a tabela estados no banco de dados
"""
from sqlalchemy import Column, Integer, String
from app.database.base import Base
from app.model.codigo_uf import CodigoUF


class Estado(Base, CodigoUF):
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True)
    sigla = Column(String, nullable=False)
    nome = Column(String, nullable=False)

    # Método construtor
    def __init__(self, id=0, sigla="", nome=""):
        super().__init__(id, sigla, nome)
