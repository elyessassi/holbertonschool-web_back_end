#!/usr/bin/env python3
"""
    Module that has a function that hashs passwords
    and the Auth class
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Method that hashs a password"""
    hashed_pw = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
    return hashed_pw


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_pw = _hash_password(password)
            newUser = self._db.add_user(email, hashed_pw)
            return newUser
        else:
            raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """method to check if the login is valid"""
        try:
            theUser = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode("UTF-8"),
                              theUser.hashed_password)
