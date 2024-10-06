#!/usr/bin/env python3
""" Module used for password hashing """
import bcrypt


def hash_password(password: str) -> bytes:
    """ function to hash a password """
    byteString = password.encode()
    hashedPWD = bcrypt.hashpw(byteString, bcrypt.gensalt())
    return hashedPWD


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ function to validate if the hashed password
     matches the real password """
    byteString = password.encode()
    return bcrypt.checkpw(byteString, hashed_password)
