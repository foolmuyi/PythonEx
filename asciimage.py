#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将一张图片根据灰度值转换为ascii字符画

from PIL import Image
import argparse

# 解析命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type = int, default = 80)
parser.add_argument('--height',type = int, default = 80)

# 获取参数
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 将灰度值映射到ascii字符
def get_char(r,g,b,alpha = 256):
	if alpha == 0:
		return ' '
	gray = int(0.2126*r + 0.7152*g + 0.0722*b)
	unit = (256 + 1)/94
	return chr(int(gray/unit) + 32)

if __name__ == '__main__':
	# 打开图片文件并转为设定的大小
	im = Image.open(IMG)
	im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

	# 按行列依次读取每一个像素并转换为ascii字符
	txt = ''
	for i in range(HEIGHT):
		for j in range (WIDTH):
			txt += get_char(*im.getpixel((j,i)))
		txt += '\n'
	print(txt)

	# 将结果写入txt文件
	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.write(txt)
	else:
		with open('output.txt','w') as f:
			f.write(txt)