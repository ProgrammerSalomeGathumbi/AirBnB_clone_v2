#!/usr/bin/python3
"""
A script that starts a Flask web application and
display a HTML page with the list of all State
objects present in DBStorage
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def hello_states_list():
    """
    Returns HTML with list of states
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
