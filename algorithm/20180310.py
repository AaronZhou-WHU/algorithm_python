#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
假如产生1的概率p，产生0的概率1-p，怎么设计产生0，1概率一样
'''
import random

def random01():
    i = random.randint(0,1)
    j = random.randint(0,1)
    if (i == 0 and j == 1):
        return 1
    elif(i == 1 and j == 0):
        return 0
    else:
        return -1

print random01()
print random01()