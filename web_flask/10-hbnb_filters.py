#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hello_hbnb_filters():
    """
    Returns HTML with hbnb_filters
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).value()
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
