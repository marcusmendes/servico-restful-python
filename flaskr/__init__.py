from flask import Flask
from flaskr.database import db_session, init_db


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    init_db()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app

