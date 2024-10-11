#!/usr/bin/env python3
""" Basic authentication module """
from api.v1.auth.auth import Auth
import base64
import binascii


class BasicAuth(Auth):
    """ basic method class"""
    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """ Method to extract base64 authorization header """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
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
        if type(base64_authorization_header) != str:
            return None
        try:
            base64.b64decode(base64_authorization_header)
        except binascii.Error:
            return None
        else:
            string = base64.b64decode(base64_authorization_header)
            return string.decode("ascii")
