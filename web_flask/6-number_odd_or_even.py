#!/usr/bin/python3
""" Imports """
from flask import Flask, escape, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number_template(n):
    """ n is number
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def show_number_odd_or_even(n):
    """ n is number
    """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run()
