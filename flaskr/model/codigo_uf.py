from sqlalchemy import Column, Integer, Date, String, ForeignKey


class CodigoUF(object):
    id = Column(Integer, primary_key=True, autoincrement=True)
    sigla = Column(String, nullable=False)
    nome = Column(String, nullable=False)

    # Ver 'problema do diamante'
    # **kwargs - parâmetros nomeados
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.sigla = kwargs['sigla']
        self.nome = kwargs['nome']

    def to_dict(self):
        return {
            "id": self.id,
            "sigla": self.sigla,
            "nome": self.nome
        }
