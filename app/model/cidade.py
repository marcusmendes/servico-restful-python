"""
Classe que representa a cidade de um endereço de uma pessoa
"""
from app.model.codigo_uf import CodigoUF


class Cidade(CodigoUF):
    # Método construtor
    def __init__(self, id=0, sigla="", nome=""):
        super().__init__(id, sigla, nome)
