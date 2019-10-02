#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''获取网页云单个歌单内所有歌曲歌词并制作词云第二版，加入协程，提高歌词获取速度'''

import os,re
import requests
import aiohttp, asyncio
from wordcloud import WordCloud
import PIL.Image as img
import numpy as np
import jieba
 
# 歌单原始url
raw_url = 'https://music.163.com/#/playlist?id=575646464'

# 伪装成浏览器请求以获取完整信息
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/77.0.3865.90 Chrome/77.0.3865.90 Safari/537.36'}

# 获取歌单内所有歌曲的链接
def get_links(raw_url):
	#　对原始url进行处理，带/#的是网页源码，不带/#的是框架源码
	pl_url = raw_url.replace(r'/#','')
	resp = requests.get(pl_url,headers=headers)
	# 用正则表达式从返回数据中匹配出歌曲名称和链接
	song_names = re.findall(r'\d+">(.*?)</a></li>',resp.text)
	song_links = re.findall(r'<li><a href="(.*?)">',resp.text)[:-2]
	return song_names,song_links

# 获取一首歌的歌词
async def get_lyric(song_link):
	async with aiohttp.ClientSession() as session:
		# 对歌曲链接进行处理，得到歌词链接
		lrc_link = song_link[:5]+'/lyric'+song_link[5:]
		lrc_url = 'https://music.163.com/api'+lrc_link+'&lv=1&kv=1&tv=-1'
		# 对获取到的原始歌词信息进行处理
		response = await session.get(lrc_url,headers=headers)
		raw_lrc = await response.text()
		lrc = '\n'.join(re.findall(r'](.*?)\\n',raw_lrc))
		return lrc

# 将歌词写入文件
async def write_lyric(lrc_path,song_name,song_link):
	print('Start downloading lyric of %s' % song_name)
	lrc = await get_lyric(song_link)
	if len(lrc) == 0:
		lrc = '纯音乐'
	with open(lrc_path,'a') as f:
		f.write(lrc)

# 获取歌词主函数
def get_lyrics(raw_url):
	song_names,song_links = get_links(raw_url)
	total_num = len(song_names)
	lrc_path = './lyrics.txt'
	# 若当前文件夹下存在上一次运行的残余文件，则删除
	if os.path.exists(lrc_path):
		os.remove(lrc_path)
	# 创建tasks，启动协程
	tasks = [asyncio.ensure_future(write_lyric(lrc_path,song_names[i],song_links[i])) for i in range(total_num)]
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait(tasks))

# 利用获取到的歌词信息制作词云
def get_wordcloud(url):
	# 去除关键词
	remove_words=[u'作词',u'作曲',u'编写',u'制作',u'Studio',u'录音棚',u'混音',u'录音室',u'编曲',u'吉他',u'弦乐',u'录音',u'la']
	with open('./lyrics.txt') as f:
		content = f.read()
		word_list = jieba.cut(content)
		purified_words = []
		for each in word_list:
			if each not in remove_words:
				purified_words.append(each)
		text = ' '.join(purified_words)
		mask = np.array(img.open('./music.jpg'))
		wc = WordCloud(
			mask=mask,
			font_path='/usr/share/fonts/truetype/arphic/ukai.ttc',
			background_color='white').generate(text)
		image = wc.to_image()
		wc.to_file('./wc'+re.findall(r'id=(\d*)',url)[0]+'.jpg')
		image.show()

def run():
	get_lyrics(raw_url)
	get_wordcloud(raw_url)

if __name__ == '__main__':
	run()
