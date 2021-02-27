from flask_seeder import Seeder, Faker, generator
from datetime import date
from app import db, Pessoa, Endereco, Cidade, Estado, Pais


# class PessoaSeeder(Seeder):
#     def run(self):
#         pais_faker = Faker(cls=Pais, init={
#             "id": generator.Integer(1, 50),
#             "sigla": generator.String(pattern="abc"),
#             "nome": generator.Name()
#         })
#
#         estado_faker = Faker(cls=Estado, init={
#             "id": generator.Integer(1, 50),
#             "sigla": generator.String(pattern="abc"),
#             "nome": generator.Name()
#         })
#
#         cidade_faker = Faker(cls=Cidade, init={
#             "id": generator.Integer(1, 50),
#             "sigla": generator.String(pattern="abc"),
#             "nome": generator.Name()
#         })
#
#         endereco_faker = Faker(cls=Endereco, init={
#             "logradouro": generator.String(),
#             "numero": generator.Integer(1, 100),
#             "cep": generator.Integer(10000000, 30000000),
#             "complemento": "",
#             "cidade": cidade_faker.create(1)[0],
#             "estado": estado_faker.create(1)[0],
#             "pais": pais_faker.create(1)[0]
#         })
#
#         pessoa_faker = Faker(cls=Pessoa, init={
#             "nome": generator.Name(),
#             "cpf": "93189451087",
#             "data_nascimento": date(1900, 1, 1),
#             "endereco": endereco_faker.create(1)[0]
#         })
#
#         for pessoa in pessoa_faker.create(5):
#             db.session.add(pessoa)


pais = Pais(id=generator.Integer(1, 50), sigla=generator.String(pattern="AB"), nome=generator.Name())
estado = Estado(id=generator.Integer(1, 50), sigla=generator.String(pattern="AB"), nome=generator.Name())
cidade = Cidade(id=generator.Integer(1, 50), sigla=generator.String(pattern="AB"), nome=generator.Name())

endereco = Endereco(logradouro=generator.String(), numero=generator.Integer(1, 100),
                    cep=generator.Integer(10000000, 30000000), cidade=cidade, estado=estado, pais=pais)

pessoa = Pessoa(generator.Name(), "93189451087", date(1900, 1, 1), endereco)

db.session.add(pessoa)
