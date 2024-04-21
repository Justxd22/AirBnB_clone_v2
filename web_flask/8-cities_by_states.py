#!/usr/bin/python3
"""Flask api HELLO."""

from flask import app, Flask, abort,  render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list():
    """HEllo."""
    return render_template('8-cities_by_states.html', x="States",
                           d=storage.all('State'))


@app.route("/cities_by_states", strict_slashes=False)
def listc():
    """HEllo."""
    return render_template('8-cities_by_states.html', x="States",
                           d=storage.all('State'))


@app.teardown_appcontext
def endd(e):
    """HEllo."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
