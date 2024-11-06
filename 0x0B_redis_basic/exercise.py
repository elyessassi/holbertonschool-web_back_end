#!/usr/bin/env python3
"""Module that implements Redis"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get_str(self, value: bytes) -> str:
        """ Converting bstring to a string """
        value = value.decode("utf-8")
        return value

    def get_int(self, value: bytes) -> int:
        """ Converting bstring to an int """
        value = int(value)
        return value

    def get(self, key: str,
            fn: Optional[Callable[[bytes], int | str]] = None) -> int | str:
        """ a Method that convertes value returned by
            redis to int or string depending
            on the arguments """
        get_value = self._redis.get(key)
        if fn:
            return fn(get_value)
        else:
            return get_value
