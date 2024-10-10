#!/usr/bin/env python3
""" Basic authentication module """
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ basic method class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method to extract base64 authorization header """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return (authorization_header[6:])
