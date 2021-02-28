from flask import Flask
from flaskr.database import db_session, init_db
from sqlalchemy.orm.exc import NoResultFound


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    init_db()

    from flaskr.controller.pessoa_controller import pessoas_blueprint
    app.register_blueprint(pessoas_blueprint)

    from flaskr.handle_errors import handle_noresultfound_exception
    app.register_error_handler(NoResultFound, handle_noresultfound_exception)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
