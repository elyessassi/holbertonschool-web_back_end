#!/usr/bin/env python3

import flask

app = flask.Flask(__name__)


@app.route("/", method="GET")
def main():
    return flask.jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
