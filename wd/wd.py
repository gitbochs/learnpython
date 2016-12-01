#coding:utf-8

import requests,re
from bs4 import BeautifulSoup

def get_r():
    url = 'http://ttmeiju.com/meiju/THE.Walking.Dead.html'
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"}
    rs = requests.get(url,headers=headers).text
    return rs

def get_download_link(rs):
    soup = BeautifulSoup(rs,'html.parser')
    link = soup.find_all(href=re.compile("FIX%E5%AD%97%E5%B9%95%E4%BE%A0"),title="ed2k高清片源")
    return link

link = get_download_link(get_r())

for l in link :
    print (l.get('href'))