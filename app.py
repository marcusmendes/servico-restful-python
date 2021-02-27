from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/webservice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
seeder = FlaskSeeder()
seeder.init_app(app, db)


class CodigoUF:
    # Método construtor
    def __init__(self, id=0, sigla="", nome=""):
        self.id = id
        self.sigla = sigla
        self.nome = nome


class Pais(db.Model, CodigoUF):
    __tablename__ = 'paises'
    id = db.Column(db.Integer, primary_key=True)
    sigla = db.Column(db.String, nullable=False)
    nome = db.Column(db.String, nullable=False)

    # Método construtor
    def __init__(self, id=0, sigla="", nome=""):
        super().__init__(id, sigla, nome)


class Estado(db.Model, CodigoUF):
    __tablename__ = 'estados'
    id = db.Column(db.Integer, primary_key=True)
    sigla = db.Column(db.String, nullable=False)
    nome = db.Column(db.String, nullable=False)

    # Método construtor
    def __init__(self, id=0, sigla="", nome=""):
        super().__init__(id, sigla, nome)


class Cidade(db.Model, CodigoUF):
    __tablename__ = 'cidades'
    id = db.Column(db.Integer, primary_key=True)
    sigla = db.Column(db.String, nullable=False)
    nome = db.Column(db.String, nullable=False)

    # Método construtor
    def __init__(self, id=0, sigla="", nome=""):
        super().__init__(id, sigla, nome)


class Endereco(db.Model):
    __tablename__ = 'enderecos'
    id = db.Column(db.Integer, primary_key=True)
    pessoa_id = db.Column(db.Integer, db.ForeignKey("pessoas.id"))
    logradouro = db.Column(db.String, nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String, nullable=True)
    cidade_id = db.Column(db.Integer, db.ForeignKey("cidades.id"))
    cidade = db.relationship("Cidade", backref="enderecos")
    estado_id = db.Column(db.Integer, db.ForeignKey("estados.id"))
    estado = db.relationship("Estado", backref="enderecos")
    pais_id = db.Column(db.Integer, db.ForeignKey("paises.id"))
    pais = db.relationship("Pais", backref="enderecos")

    # Método construtor
    def __init__(self, cep="", logradouro="", numero=0, complemento="", cidade: Cidade = "", estado: Estado = "", pais: Pais = ""):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.pais = pais


class Pessoa(db.Model):
    __tablename__ = 'pessoas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    endereco = db.relationship("Endereco", uselist=False, backref=db.backref("pessoas", lazy=True))

    # Método construtor
    def __init__(self, nome="", cpf="", data_nascimento="", endereco: Endereco = ""):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
