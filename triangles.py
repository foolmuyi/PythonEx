#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#杨辉三角生成器
# my solution
def triangles():
	m = 1
	while True:
		if m == 1:
			result = [1]
		elif m == 2:
			result = [1,1]
		else:
			mid = result
			result = []
			result.append(1)
			for n in range(1,m-1):
				result.append(mid[n-1] + mid[n])
			result.append(1)
		m = m + 1
		yield result


# dalao's solution  orz
def triangles():
    L = [1]
    while 1:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]