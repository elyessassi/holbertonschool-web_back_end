#!/usr/bin/env python3
""" Session authentication module """
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """ Session authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ method that creates a session"""
        if user_id is None:
            return None
        if not (isinstance(user_id, str)):
            return None
        sessionID = str(uuid4())
        self.__class__.user_id_by_session_id[sessionID] = user_id
        return sessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ A method for retrieving user ID using
            session ID"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.__class__.user_id_by_session_id.get(f"{session_id}")

    def current_user(self, request=None):
        """ A method that gets current user instance
         by using session_cookie method and
         user_id_by_session_id dictionnary"""
        cookie_value = self.session_cookie(request)
        userID = self.user_id_by_session_id[f"{cookie_value}"]
        return User.get(userID)
