#!/usr/bin/env python3

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    def put(self, key, item):
        if (key != None and item != None):
            self.cache_data[key] = item
    def get(self, key):
        if (key != None):
            return (self.cache_data[key])
        else:
            return (None)