# -*- coding: utf-8 -*-
# @time: 2020-04-06 18:31
# @file: stream.py

class Stream(object):
    
    def __init__(self, first, second):
        assert callable(second), "must be callable"
        self.first = first
        self.second = second
    
    @property
    def rest(self):
        if self.second is not None:
            self._rest = self.second()
            self.second = None
        return self._rest
        
if __name__ == '__main__':
    s = Stream(0, lambda : Stream(1, lambda :Stream(2)))
    print()