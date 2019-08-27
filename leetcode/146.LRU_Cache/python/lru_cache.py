#/usr/bin/env python
# -*- coding: utf-8 -*-
import collections

class LRUCache(object):

    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v
        return v
    
    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value


if __name__ == '__main__':
    cache = LRUCache(5)
    cache.put(1, 1)
    cache.put(2, 2)
    print cache.get(1)     # returns 1
    cache.put(3, 3)   # evicts key 2
    print cache.get(2)      # returns -1 (not found)
    cache.put(4, 4)    # evicts key 1
    print cache.get(1)       # returns -1 (not found)
    print cache.get(3)    # returns 3
    print cache.get(4)       # returns 4
