from flaskr.database import db_session
from datetime import date
from flaskr.model.pessoa import Pessoa
from flaskr.model.endereco import Endereco
from flaskr.model.cidade import Cidade
from flaskr.model.estado import Estado
from flaskr.model.pais import Pais


cidade1 = Cidade(id=1, sigla="LW", nome="Little Whinging")
estado1 = Estado(id=1, sigla="SU", nome="Surrey,")
pais1 = Pais(id=1, sigla="UK", nome="United Kingdom")
endereco1 = Endereco(cep="22793220",  logradouro="Privet Drive", numero="4", complemento="",
                     cidade=cidade1, estado=estado1, pais=pais1)
pessoa1 = Pessoa(nome="The Dursleys", cpf="35681193071", data_nascimento=date(1988, 1, 1), endereco=endereco1)

db_session.add_all([pessoa1])
db_session.commit()
db_session.close()
