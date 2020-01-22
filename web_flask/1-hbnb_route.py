#!/usr/bin/python3
""" Imports """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Greeting
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Greeting
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run()
