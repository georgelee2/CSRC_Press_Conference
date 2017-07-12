# -*- coding: utf-8 -*-
# 抓取证监会新闻发布会页面的内容

import urllib.request
from bs4 import BeautifulSoup
import re
import time
from urllib.error import HTTPError

home = "http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwfbh/index.html"

def open_url_b(url):
	headers = {}
	headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
	req = urllib.request.Request(url, headers=headers) 
	html = urllib.request.urlopen(req)
	bs0bj = BeautifulSoup(html,'lxml')
	return bs0bj

def get_url(url):
	bs0bj = open_url_b(url)
	text = bs0bj.find('body').find('div', {'class':"body_bk"}).find('div', {'class':"body"}).find('div', {'class':"er_main"}).find('div', {'class':"er_right"})
	address = text.find_all('a',href=re.compile("(\.\/)[0-9]+\/[0-9a-zA-Z_]+\.(html|htm)"))
	return address # 返回的是目录页中包含的新闻发布会公告的link

def get_save_message(url):
	address = get_url(url)
	for add in address:
		url_0 = add['href']
		url = "http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwfbh" + url_0[1:]
		bs0bj = open_url_b(url)
		text = bs0bj.find('head').find('title')
		a = text.get_text()
		if '新闻发布会' in a: 
			txt = bs0bj.find('body').find('div',{'class':"in_main"})
			b = txt.get_text()
			content = a + b
			filename = a + '.txt'
			with open(filename, 'wb') as f:
				f.write(content.encode('utf-8')) # str写入txt，可以用bytes模式写入，所以open要以'wb'打开
				f.close()

if __name__ == "__main__":
	get_save_message(home)
	time.sleep(3)
	for i in range(1,10):
		home_url = "http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwfbh/index_" + str(i) + '.html'
		try:
			get_save_message(home_url)
		except HTTPError as e:
			print(e)
		else:
			print(home_url)
		time.sleep(3)