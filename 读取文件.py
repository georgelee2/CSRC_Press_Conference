# -*- coding: utf-8 -*-
# 提取证监会历史新闻发布会中与keyword相关的内容
import os

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    return pathDir

def read_txt(filename):
	keyword_0 = "XXX"
	keyword = keyword_0.encode('utf-8')
	with open(filename,'rb') as f:
		for line in f.readlines():
			if keyword in line:
				content = filename + '\n' + line.decode('utf-8')
				return content

if __name__ == '__main__':
    filepath = "E:\\python\\py3\\p\\x\\证监会\\新闻发布会\\新闻发布会文件" # 需修改为本地地址
    pathDir = eachFile(filepath)
    lista = []
    for allDir in pathDir:
    	filename = "E:\\python\\py3\\p\\x\\证监会\\新闻发布会\\新闻发布会文件\\" + allDir # 需修改为本地地址
    	content = read_txt(filename)
    	if isinstance(content, str):
    		lista.append(content)
            
    text = ''.join(lista)
    print (text.count("E:\\python\\py3\\p\\x\\证监会\\新闻发布会\\新闻发布会文件\\")) # 需修改为本地地址
    with open("XXX.txt", 'wb') as f:
    	f.write(text.encode('utf-8'))