#!/usr/bin/env python3
"""Module that implements Redis"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator used to count calls """
    @wraps(method)
    def wrapper(self, *args: Any) -> Any:
        """ Wrapper function """
        self._redis.incr(method.__qualname__)
        return method(self, *args)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ decorator used to store inputs and outputs """
    @wraps(method)
    def wrapper(self, *args: Any) -> Any:
        """ Wrapper function """
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        op = method(self, *args)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(op))
        return op

    return wrapper


class Cache():
    """Caching Class"""
    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
            fn: Optional[Callable] = None) -> Union[int, str]:
        """ A Method that convertes value returned by
            redis to int or string depending
            on the arguments """
        get_value = self._redis.get(key)
        if fn:
            return fn(get_value)
        else:
            return get_value


def replay(method: Callable):
    """ Function that shows method calling history """
    cacheobj = method.__self__
    length = cacheobj.get(method.__qualname__, cacheobj.get_int)
    inputs = cacheobj._redis.lrange(f"{method.__qualname__}:inputs", 0, -1)
    outputs = cacheobj._redis.lrange(f"{method.__qualname__}:outputs", 0, -1)
    zipped = zip(inputs, outputs)
    IOlist = list(zipped)
    print(f"Cache.store was called {length} times:")
    for i in range(length):
        print(f"Cache.store(*{IOlist[i][0].decode()}) -> {IOlist[i][1]}")
