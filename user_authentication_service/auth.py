#!/usr/bin/env python3
"""
    Module that has a function that hashs passwords
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """ Method that hashs a password"""
    hashed_pw = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
    return hashed_pw
