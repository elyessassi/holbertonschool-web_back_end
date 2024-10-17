#!/usr/bin/env python3
"""
    Creating a flask app and defining
    routes
"""
import flask
from auth import Auth

AUTH = Auth()
app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def main() -> flask.Response:
    """ method that converts a dict into a JSON response
         and returns it
    """
    return flask.jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """Method to register users using the Auth class method"""
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return flask.jsonify({"message": "email already registered"})
    else:
        return flask.jsonify({"email": f"{email}", "message":
                              "user created"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
