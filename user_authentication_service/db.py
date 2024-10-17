#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User
from user import Base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Method that creates a user """
        newUser = User(email=email, hashed_password=hashed_password)
        newSession = self._session
        newSession.add(newUser)
        newSession.commit()
        return newUser

    def find_user_by(self, **kwargs):
        """Method that finds the wanted User
            using keyword arguments"""
        newSession = self._session
        wantedUser = newSession.query(User).filter_by(**kwargs).first()
        if wantedUser is None:
            raise NoResultFound
        return wantedUser
