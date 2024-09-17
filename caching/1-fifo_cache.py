#!/usr/bin/env python3

""" FIFO Caching Algorithm"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):

    """
    put: adding a key value pair in the dictionnary
    get: getting the value of a key specified in the dictionnary
    """

    def put(self, key, item):
        """ adding an item """
        if (key is not None and item is not None):
            if (len(self.cache_data) < BaseCaching.MAX_ITEMS):
                self.cache_data[key] = item
            else:
                mylist = list(self.cache_data)
                print(f"DISCARD: {mylist[0]}")
                del self.cache_data[mylist[0]]
                self.cache_data[key] = item

    def get(self, key):
        """ displays an item of a certain key"""
        if (key is not None or key not in self.cache_data):
            return (None)
        else:
            return (self.cache_data[key])
