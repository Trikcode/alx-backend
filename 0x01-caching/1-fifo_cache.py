#!/usr/bin/env python3
""" BaseCaching module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.cache_data = {}
        self.cache_order = []

    def put(self, key, item):
        """ Store a key-value pair """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_order)
            if length >= BaseCaching.MAX_ITEMS and key in self.cache_data.keys():
                del self.cache_data[self.cache_order[0]]
                del self.cache_order[0]
            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """ Return value linked to key.
        If key is None or doesn't exist, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
