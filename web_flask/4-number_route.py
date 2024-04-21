#!/usr/bin/python3
"""Flask api HELLO."""

from flask import app, Flask, abort

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


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def echov2(text):
    """HEllo."""
    x = text.replace("_", " ")
    return f"Python {x}"


@app.route("/number/<n>", strict_slashes=False)
def num(n):
    """HEllo."""
    try:
        x = int(n)
        return f"{n} is a number"
    except Exception as e:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
