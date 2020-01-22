#!/usr/bin/python3
""" Imports """
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Greeting
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """ C is Fun
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run()
