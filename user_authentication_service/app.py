#!/usr/bin/env python3
"""
    Creating a flask app and defining
    routes
"""
import flask

app = flask.Flask(__name__)


@app.route("/", method="GET")
def main() -> flask.Response:
    """ method that converts a dict into a JSON response
         and returns it
    """
    return flask.jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
