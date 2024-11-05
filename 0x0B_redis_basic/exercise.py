#!/usr/bin/env python3
"""Module that implements Redis"""
import redis
import uuid
from typing import Union


class Cache():
    """Caching Class"""
    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that stores data as a value of
            of a randomly generated key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
