#!/usr/bin/python3
""" C is Fun """

from flask import Flask, render_template

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


@app.route('/number_template/<int:n>')
def numbersandtemplates(n):
    """ return message """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ return message """
    if (n % 2) == 0:
        xd = "even"
    else:
        xd = "odd"
    return render_template('6-number_odd_or_even.html', n=n, xd=xd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
