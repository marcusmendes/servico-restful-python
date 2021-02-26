from flask import Flask
from app.database.create_database import create_database

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == '__main__':
    create_database()
    app.run(debug=True)
