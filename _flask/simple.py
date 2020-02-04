"""A simple flask app serving 'Hello world'"""

from flask import Flask


APP_NAME = __name__  # default __name__
HOST = '0.0.0.0'     # default '0.0.0.0'
PORT = 8080          # default 8080

APP = Flask(APP_NAME)


@APP.route('/')
def hello_world():
    """Returns hello world"""
    return 'Hello, World!'


APP.run(host=HOST, port=PORT)
