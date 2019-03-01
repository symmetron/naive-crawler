#coding=UTF-8
from bs4 import BeautifulSoup
import requests

#最简单的爬一篇文章，不涉及翻页

if __name__=='__main__':
    target='https://www.douban.com/note/559435835/'
    req=requests.get(url=target)                    #获取html
    html=req.text
    #处理数据
    bfsp=BeautifulSoup(html,'html.parser')          #有些教程里没有'html.parser'指定解析器，貌似不行
    article_tag=bfsp.find_all('div',class_="note",id="link-report")
    #article=article_tag[0].contents                #找到tag之后取出作为子节点的string--是很多<br/>和字符串组成的list
    article=article_tag[0].get_text()               #这样可以取得文本

    #文件写入
    fp = open('article.txt','w')                    #存在则写入，不存在先创建一个
    fp.write(article)
    fp.close()
