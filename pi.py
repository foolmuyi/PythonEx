#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#利用Python自带的itertools模块计算pi的值

import itertools


# my solution
def pi(N):
	odd = itertools.count(1,2)  # 创建一个奇数序列: 1, 3, 5, 7, 9, ...
	N_odd = itertools.takewhile(lambda x: x < 2*N, odd)  # 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
	res = []
	for i in range(N):
		res.append((-1)**i*4*(1/next(N_odd)))  # 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
	result = sum(res)  # 求和
	return result


# dalao solution  tqltql
# def pi(N):
#     cs = itertools.cycle([4,-4])
#     odd = itertools.count(1,2)
#     sum = 0
#     for i in range(N):
#         sum += (next(cs)/next(odd))
#     return sum



print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))