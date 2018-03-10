#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
假如产生1的概率p，产生0的概率1-p，怎么设计产生0，1概率一样
'''

#非递归
def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a

# 输出了第10个斐波那契数列
print fib(10)

#递归
def fib(n):
	if n==1 or n==2:
		return 1
	return fib(n-1)+fib(n-2)

# 输出了第10个斐波那契数列
print fib(10)

