#!/usr/bin/python3
"""Starts the Flask web application.
application that listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with the list of all the State objects.
    /states/<id>: HTML page displays a given state with the <id>.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays the HTML page with the list of every States.
    States they are sorted by a name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays the HTML page with the info about the <id>, if it does exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Removes current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
