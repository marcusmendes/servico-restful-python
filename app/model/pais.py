"""
Classe que representa um país de um endereço de uma Pessoa
"""
from app.model.codigo_uf import CodigoUF


class Pais(CodigoUF):
    # Método construtor
    def __init__(self, id=0, sigla="", nome=""):
        super().__init__(id, sigla, nome)
