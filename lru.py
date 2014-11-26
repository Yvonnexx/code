#!/usr/bin/python

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru = {}
        self.tm = 0

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            old_key = min(self.lru.items(), key = lambda x:x[1])[0]
            self.lru.pop(old_key)
            self.cache.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1

cache = LRUCache(1)
cache.set(2,1)
print cache.get(2)
cache.set(3,2)
print cache.get(2)
print cache.get(3)

