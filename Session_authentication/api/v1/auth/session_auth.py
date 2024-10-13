#!/usr/bin/env python3
""" Session authentication module """
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Session authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ method that creates a session"""
        if user_id is None:
            return None
        if not (isinstance(user_id, str)):
            return None
        sessionID = uuid4()
        self.__class__.user_id_by_session_id[sessionID] = user_id
        return sessionID
