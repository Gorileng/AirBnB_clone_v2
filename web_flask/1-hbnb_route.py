#!/usr/bin/python3
"""Starts the flask web app
Routes:
    / - displays the "Hello HBNB!"
    /hbnb - displays the "HBNB"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """prints the Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints the HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
