#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


os.chdir('/home/muyi/testofos')

#列出当前目录及其子目录内的所有文件（遇到隐藏文件好像会出问题）
def list_all_files(mydir):
	all_file = []
	dirs = [mydir]
	while len(dirs) > 0:
		for each_dir in dirs:
			dirs.remove(each_dir)
			each_dir_files = os.listdir(each_dir)
			for file in each_dir_files:
				file_path = os.path.join(each_dir,file)
				if os.path.isfile(file_path):
					all_file.append(file_path)
				else:
					dirs.append(file_path)
	return all_file

#在当前目录及其子目录内查找文件名含有指定字符的文件
def search_file(text):
	all_files = list_all_files(os.getcwd())
	target_file = []
	for f in all_files:
		if text in os.path.splitext(f)[0]:
			target_file.append(os.path.relpath(f))
		else:
			pass
	return target_file


print(list_all_files(os.getcwd()))
print(search_file('test'))