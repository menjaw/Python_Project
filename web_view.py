from flask import Flask, render_template, Response

app = Flask(__name__)


def initialize():
    return app


def run_program():
    return app.run(debug=True, port=3000)

