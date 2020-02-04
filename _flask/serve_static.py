"""A simple flask app serving a file"""

from flask import Flask


APP_NAME = __name__  # default __name__
HOST = '0.0.0.0'     # default '0.0.0.0'
PORT = 8080          # default 8080

APP = Flask(APP_NAME)


@APP.route('/')
def serve_file():
    """Returns a file"""
    return APP.send_static_file('serve_static.html')


APP.run(host=HOST, port=PORT)
