#!/usr/bin/env python3
""" lru cach module """


from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ put """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                popped = self.queue.popleft()
                del self.cache_data[popped]
                print("DISCARD: " + str(popped))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key, None)
