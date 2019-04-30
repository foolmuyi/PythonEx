#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


def pi(N):
	odd = itertools.count(1,2)  # 创建一个奇数序列: 1, 3, 5, 7, 9, ...
	N_odd = itertools.takewhile(lambda x: x < 2*N, odd)  # 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
	res = []
	for i in range(N):
		res.append((-1)**i*4*(1/next(N_odd)))  # 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
	result = sum(res)  # 求和
	return result



print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))