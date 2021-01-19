#!/usr/bin/python3
""" C is Fun """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def Index():
    """ return message """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """ return message """
    return 'HBNB'

@app.route('/c/<text>')
def C(text):
    """ return message """
    return 'C ' + text.replace('_', ' ')

@app.route('/python/<text>')
@app.route('/python')
def python(text='is cool'):
    """ return message """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>')
def number(n):
    """ return message """
    return "{:d} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
