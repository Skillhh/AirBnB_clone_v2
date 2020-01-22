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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text='is cool'):
    """ Python is cool
    """
    return 'Python {}'.format(escape(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """ n is number
    """
    return '{} is a number'.format(escape(n))


if __name__ == '__main__':
    app.run()
