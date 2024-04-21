#!/usr/bin/python3
"""Flask api HELLO."""

from flask import app, Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """HEllo."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def bnb():
    """HEllo."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def echo(text):
    """HEllo."""
    x = text.replace("_", " ")
    return f"C {x}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
