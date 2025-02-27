#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """
    instance that return root page
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
    instance that returns /hbnb content
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_c(text):
    """
    instance that returns /c content
    """
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_python(text='is cool'):
    """
    instance that returns /python content
    """
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def hello_num(n):
    """
    instance that returns /number content
    """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello_html(n):
    """
    instance that returns html page
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def hello_odd(n):
    """
    instance that returns odd or even number as a h1
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
