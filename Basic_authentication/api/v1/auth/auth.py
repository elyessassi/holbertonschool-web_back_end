#!/usr/bin/env python3
""" authentication file """
from flask import request
from typing import List
from typing import TypeVar


class Auth():
    """ Authentication file"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if accessing a path
        requires authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to check the authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to check the current user """
        return None
