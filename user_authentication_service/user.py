#!/usr/bin/env python3
""" module that has the User class """
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ User class that create the table users """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
