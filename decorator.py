#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

def metric(fn):
	def wrapper(*args,**kw):
		start_time = time.time()
		fn(*args,**kw)
		end_time = time.time()
		print('%s executed in %s ms' % (fn.__name__, end_time-start_time))
		return fn(*args,**kw)
	return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
print(f)
print(s)