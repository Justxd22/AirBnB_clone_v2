#!/usr/bin/python3
"""Flask api HELLO."""

from flask import app, Flask, abort,  render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def list():
    """HEllo."""
    return render_template('10-hbnb_filters.html',
                           storage=storage.all('State'),
                           amens=storage.all('Amenity'))


@app.teardown_appcontext
def endd(e):
    """HEllo."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
