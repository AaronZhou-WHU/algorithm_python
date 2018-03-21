#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
符号匹配
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        hash={"]":"[", "}":"{" , ")":"("}
        for char in s:
            if(char in hash.values()):
                 stack.append(char)
            elif(char in hash.keys()):
                if(stack==[] or hash[char] != stack.pop()):
                    return False
            else:
                return False
        return stack==[]