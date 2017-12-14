import requests
from bs4 import BeautifulSoup
import re
def top_trending():
        url='https://in.reuters.com/news/top-news'
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'html.parser')
        links=soup.find_all(href=re.compile('/article/'))
        news=[]
        for i in links:
#                print i
                print str(links.index(i))+')'+i.text

top_trending()
