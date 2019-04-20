#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

# my solution
def to_timestamp(dt_str, tz_str):
    re_tz = re.match(r'UTC([\+\-]{1})(\d+)\:\d{2}',tz_str)
    tz = int(re_tz.group(2))
    dt_local = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    if re_tz.group(1) == '+':
    	dt_bj = dt_local - timedelta(hours = tz-8)
    elif re_tz.group(1) == '-':
    	dt_bj = dt_local + timedelta(hours = tz+8)
    else:
    	print('wrong format')
    return dt_bj.timestamp()

# # dalao's solution
# def to_timestamp(dt_str, tz_str):
#     tz_num = re.match('^UTC([\+|-]\d+):00', tz_str)
#     tz_int = int(tz_num.group(1))
#     dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
#     c_dt = dt.replace(tzinfo=timezone(timedelta(hours=tz_int)))
#     return c_dt.timestamp()


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')