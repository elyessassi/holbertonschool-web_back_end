#!/usr/bin/env python3

""" MRU Caching Algorithm"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):

    """
    put: adding a key value pair in the dictionnary
    get: getting the value of a key specified in the dictionnary
    """

    def put(self, key, item):
        """ adding an item """
        if (key is not None and item is not None):
            if (key in self.cache_data):
                del self.cache_data[key]
                self.cache_data[key] = item
            else:
                if (len(self.cache_data) < BaseCaching.MAX_ITEMS):
                    self.cache_data[key] = item
                else:
                    mylist = list(self.cache_data)
                    print(f"DISCARD: {mylist[-1]}")
                    del self.cache_data[mylist[-1]]
                    self.cache_data[key] = item

    def get(self, key):
        """ displays an item of a certain key"""
        if (key is None or key not in self.cache_data):
            return (None)
        else:
            if (key in self.cache_data):
                tempItem = self.cache_data[key]
                del self.cache_data[key]
                self.cache_data[key] = tempItem
            return (self.cache_data[key])
