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
def users() -> flask.Response:
    """Method to register users using the Auth class method"""
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return flask.jsonify({"message": "email already registered"}), 400
    else:
        return flask.jsonify({"email": f"{email}", "message":
                              "user created"}), 200


@app.route("/sessions", methods=["POST"])
def login() -> flask.Response:
    """ Method that logs users in
        (checks for credentials and
        creates sessions)"""
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    theUser = AUTH.valid_login(email, password)
    if theUser is False:
        flask.abort(401)
    theId = AUTH.create_session(email)
    Response = flask.make_response(flask.jsonify({"email": f"{email}",
                                                  "message":
                                                  "logged in"}))
    Response.set_cookie("session_id", theId)
    return Response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
