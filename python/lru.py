# -*- coding: utf-8 -*-
# @time: 2020-05-27 11:23
# @file: lru.py

from collections import OrderedDict

class LRU(object):
    
    def __init__(self, capacity):
        self.lru = OrderedDict()
        self.capacity = capacity
    
    def put(self, key, value):
        if key in self.lru:
            self.lru.move_to_end(key)
        self.lru[key] = value
        if len(self.lru) > self.capacity:
            self.lru.popitem(last=False)
    
    def get(self, key):
        if key in self.lru:
            self.lru.move_to_end(key)
            return self.lru[key]
        return -1




lru = OrderedDict()
lru["1"] = 1
lru["2"] = 1
lru["3"] = 1
