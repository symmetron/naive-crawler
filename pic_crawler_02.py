#coding=UTF-8
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import random

#这个是可以获取多个页面的版本，实际不太行——会被封ip
target=('https://e-hentai.org/g/1373291/f433228872/')
req=requests.get(url=target)                #获取html
html=req.text
bfsp=BeautifulSoup(html,'html.parser')
category_tag=bfsp.find('div',id='gdt')      #获取目录
page_num=len(category_tag.contents)-1
for page_index in range(page_num):
    single_page=category_tag.contents[page_index]
    a_tag=single_page.find('a')
    target_href=a_tag['href']                           #获取子页面的链接地址
    single_req=requests.get(url=target_href)            #获取子页面的html
    single_html=single_req.text
    single_bfsp=BeautifulSoup(single_html,'html.parser')
    single_img_tag=single_bfsp.find('img',id='img')
    single_url=single_img_tag['src']
    urllib.request.urlretrieve(single_url,'D:\output\Image_Processing\pic_%s.jpg'%page_index)
    time.sleep(random.randint(5,10))
