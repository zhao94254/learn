# -*- coding: utf-8 -*-
# @time: 2020-04-16 18:30
# @file: rate_limit.py

import time


class Funnel(object):
    
    def __init__(self, capacity, rate):
        """
        
        :param capacity: 漏斗容量
        :param rate: 1s 可以滴多少
        """
        self.capacity = capacity # 漏斗容量
        self.rate = rate # 速率
        self.last_timer = time.time() #
        self.cur = capacity
        
    def allow(self):
        self.make_space()
        if self.cur > 0:
            self.cur -= 1
            return True
        return False
    
    def make_space(self):
        now_ts = time.time()
        delta = now_ts - self.last_timer # 上一次滴水时间到现在的间隔
        self.cur += delta*self.rate # 还可以滴多少
        if self.cur > self.capacity:
            self.cur = self.capacity
        self.last_timer = now_ts

if __name__ == '__main__':
    fl = Funnel(10, 5)
    for i in range(100):
        time.sleep(0.05)
        print(fl.allow(), i)