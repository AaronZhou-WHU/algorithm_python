#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
解法1
'''
a = int(raw_input("请输入一个数字:\n"))
x = str(a)
flag = True

for i in range(len(x) / 2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print "%d 是一个回文数!" % a
else:
    print "%d 不是一个回文数!" % a

'''
解法2
'''
def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    tmp = x
    y = 0
    while tmp:
        y = y * 10 + tmp % 10
        tmp = tmp / 10
    return y == x

'''
解法3
'''
def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0: return False
    s = str(x)
    return s == s[::-1]