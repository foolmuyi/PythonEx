#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    #返回指定分数区间的名字，按分数从低到高排序
    try:
	    conn = sqlite3.connect(db_file)
	    cursor = conn.cursor()
	    cursor.execute('select * from user where score>=? and score<=?',(low,high))
	    values = cursor.fetchall()
    except:
	    pass
    finally:
	    cursor.close()
	    conn.close()
	# 冒泡排序，大力出奇迹
    count = len(values)
    for i in range(0,count):
    	for j in range(i+1,count):
    		if values[i][2] > values[j][2]:
    			values[i],values[j] = values[j],values[i]
    result = []
    for k in range(0,count):
    	result.append(values[k][1])
    return result


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')