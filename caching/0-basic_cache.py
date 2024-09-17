#!/usr/bin/env python3

""" Basic Caching """

from base_caching import BaseCaching


class BasicCache(BaseCaching):

    """
    put: adding a key value pair in the dictionnary
    get: getting the value of a key specified in the dictionnary
    """

    def put(self, key, item):
        """ adding an item """
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """ displayns an item of a certain key"""
        if (key is not None or key not in self.cache_data):
            return (None)
        else:
            return (self.cache_data[key])
