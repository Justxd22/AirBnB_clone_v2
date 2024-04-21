#!/usr/bin/python3
"""Flask api HELLO."""

from flask import app, Flask, abort,  render_template

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


@app.route("/number_template/<n>", strict_slashes=False)
def template(n):
    """HEllo."""
    try:
        x = int(n)
        return render_template('5-number.html', n=n)
    except Exception as e:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def evenodd(n):
    """HEllo."""
    try:
        x = int(n)
        t = "odd" if (x % 2) else "even"
        return render_template('6-number_odd_or_even.html', n=n, type=t)
    except Exception as e:
        print(e)
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
