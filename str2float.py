#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
	a,b = s.split('.')
	DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	def char2num(s):
		return DIGITS[s]
	def fn(x,y):
		return x*10 + y
	a_num = reduce(fn,map(char2num,a))
	b_num = reduce(fn,map(char2num,b))
	c_num = 10**len(str(b))
	return a_num + b_num/c_num



print(str2float('123.456'))