#!/usr/bin/env python3
"""
    Module that has a function that hashs passwords
    and the Auth class
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """ Method that hashs a password"""
    hashed_pw = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
    return hashed_pw


def _generate_uuid() -> str:
    """ Method that generates a unique id"""
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """ method that creates a session and adds session id
        to user """
        try:
            theUser = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            theId = _generate_uuid()
            theUser.session_id = theId
            self._db._session.commit()
        return theId

    def get_user_from_session_id(self, session_id: str) -> User | None:
        """ method that gets user by session_id """
        try:
            theUser = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        except InvalidRequestError:
            return None
        else:
            return theUser
