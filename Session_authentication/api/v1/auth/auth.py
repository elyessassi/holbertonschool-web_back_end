#!/usr/bin/env python3
""" authentication file """
from flask import request
from typing import List
from typing import TypeVar

SESSION_NAME = "_my_session_id"


class Auth():
    """ Authentication blueprint"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if accessing a path
        requires authentication """
        # will return True if path is not in the list
        # else it will return false
        if path is None:
            return True
        if (excluded_paths is None or excluded_paths == []):
            return True
        if (path in excluded_paths or (path + "/") in excluded_paths):
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Method to check the authorization header """
        if request is None:
            return None
        if request.headers.get("Authorization"):
            return request.headers.get("Authorization")
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to check the current user """
        return None

    def session_cookie(self, request=None):
        """ Method to get session cookies"""
        if request is None:
            return None
        return request.cookies.get(SESSION_NAME)
