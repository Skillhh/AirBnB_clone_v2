#!/usr/bin/python3
from flask import Flask, escape, request

app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/')
def hello():
    name = request.args.get("name",'HBNB')
    return 'Hello {}!'.format(escape(name))
