#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
找出一个字符串数组中所有字符串的最长公共前缀
'''


'''
方法1
'''
def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    strs.sort()
    res = ''
    for i in xrange(len(strs[0])):
        if i >= len(strs[-1]) or strs[-1][i] != strs[0][i]:
            return res
        res += strs[0][i]
    return res

'''
方法2
'''
import os
def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    return os.path.commonprefix(strs)