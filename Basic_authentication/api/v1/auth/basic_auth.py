#!/usr/bin/env python3
""" Basic authentication module """
from api.v1.auth.auth import Auth
import base64
import binascii
from typing import TypeVar
from models.user import User
from models.base import DATA


class BasicAuth(Auth):
    """ basic method class"""
    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """ Method to extract base64 authorization header """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return (authorization_header[6:])

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ method to decode base64 """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64.b64decode(base64_authorization_header)
        except binascii.Error:
            return None
        else:
            string = base64.b64decode(base64_authorization_header)
            return string.decode("ascii")

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str
                                 ) -> (str, str):
        """ method to extract user credentials
         form the decoded authorization header
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not (isinstance(decoded_base64_authorization_header, str)):
            return (None, None)
        index = decoded_base64_authorization_header.find(":")
        # index is the index of ':' in the string
        if index == -1:
            return (None, None)
        else:
            # will return the part before ':'
            # and after ':'
            return (decoded_base64_authorization_header[:index],
                    decoded_base64_authorization_header[index + 1:])

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd:
                                     str) -> TypeVar('User'):
        if (user_email is None) or (not isinstance(user_email, str)):
            return None
        if (user_pwd is None) or (not isinstance(user_pwd, str)):
            return None
        if DATA["User"] == {}:
            return None
        if not (User.search({"email": f"{user_email}"})):
            return None
        # I will get the instance of User class
        # that have the wanted email
        the_user = (User.search({"email": f"{user_email}"}))[0]
        if not the_user.is_valid_password(user_pwd):
            return None
        else:
            return the_user
