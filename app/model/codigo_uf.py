"""
Classe mãe que representa os código de UF
"""


class CodigoUF:
    # Método construtor
    def __init__(self, id=0, sigla="", nome=""):
        self._id = id
        self._sigla = sigla
        self._nome = nome

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def sigla(self):
        return self._sigla

    @sigla.setter
    def sigla(self, sigla: str):
        self._sigla = sigla

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
