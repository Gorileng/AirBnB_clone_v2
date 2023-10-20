#!/usr/bin/python3
"""Starts the flask web app
Routes:
    / - displays the "Hello HBNB!"
    /hbnb - displays the "HBNB"
    /c/<text> - displays the "C <text>"
    /python/<text> - displays the "Python is cool"
    /number/<n> - displays n if it the integer
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """prints the Hello HBNB"""
    return "Hello the HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints the HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """prints C then followed by the <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """prints the Python is cool"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """displays n if it is the integer"""
    return "%i is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0")
