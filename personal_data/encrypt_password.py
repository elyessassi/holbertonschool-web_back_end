#!/usr/bin/env python3
""" Module used for password hashing """
import bcrypt


def hash_password(password: str) -> bytes:
    """ function to hash a password """
    byteString = password.encode()
    hashedPWD = bcrypt.hashpw(byteString, bcrypt.gensalt())
    return hashedPWD
