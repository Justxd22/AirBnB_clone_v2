#!/usr/bin/python3
"""Flask api HELLO."""

from flask import app, Flask, abort,  render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list():
    """HEllo."""
    return render_template('9-states.html', d=None,
                           storage=storage.all('State'))


@app.route("/states/<id>", strict_slashes=False)
def listc(id):
    """HEllo."""
    d = storage.all('State').get('State.{}'.format(id))
    return render_template('9-states.html', d=d, storage=None)


@app.teardown_appcontext
def endd(e):
    """HEllo."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
