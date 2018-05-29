from flask import *

app = Flask(__name__)


def initialize():
    return app


def run_program():
    return app.run(debug=True, port=3000)

