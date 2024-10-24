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


@app.route("/sessions", methods=["DELETE"])
def logout() -> None:
    """Method used to logout the user"""
    SessionID = flask.request.cookies.get("session_id")
    theUser = AUTH.get_user_from_session_id(SessionID)
    if theUser is None:
        flask.abort(403)
    else:
        AUTH.destroy_session(theUser.id)
        return flask.redirect('/')


@app.route("/profile", methods=["GET"])
def profile() -> None:
    SessionID = flask.request.cookies.get("session_id")
    theUser = AUTH.get_user_from_session_id(SessionID)
    if theUser is None:
        flask.abort(403)
    return flask.Response({"email": f"{theUser.email}"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
