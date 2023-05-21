#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def hello_states():
    """ returns HTML page with list of states"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def hello_states_id(id):
    """ returns id if it exists"""
    for states in storage.all("State").value():
        if state.id == id:
            return render_template("9-states.html", states=states)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
