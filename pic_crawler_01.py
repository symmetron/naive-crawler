#coding=UTF-8
from bs4 import BeautifulSoup
import requests
import urllib.request

#最简单的爬一张图片，不涉及翻页
target=('https://e-hentai.org/s/e56538dbed/1373291-2')
req=requests.get(url=target)                #获取html
html=req.text
#处理数据
bfsp=BeautifulSoup(html,'html.parser')
img_tag=bfsp.find('img',id='img')
url=img_tag['src']
#url=url.replace('../../..','http://www.coe.pku.edu.cn')有些时候url需要拼接补全

urllib.request.urlretrieve(url,'D:\output\Image_Processing\pic.jpg')            #保存图片到本地（windows正反斜杠路径没区别）
