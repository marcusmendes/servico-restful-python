from flask import Flask
from flaskr.database import db_session, init_db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    init_db()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
    
    from flaskr.controller.Cidades import cidades_blueprint
    app.register_blueprint(cidades_blueprint)
    from flaskr.controller.Paises import paises_blueprint
    app.register_blueprint(paises_blueprint)
    from flaskr.controller.Estados import estados_blueprint
    app.register_blueprint(estados_blueprint)
    from flaskr.controller.Enderecos import enderecos_blueprint
    app.register_blueprint(enderecos_blueprint)
    from flaskr.controller.Pessoas import pessoas_blueprint
    app.register_blueprint(pessoas_blueprint)

    return app
