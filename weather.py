import requests
from bs4 import BeautifulSoup

url = "http://www.weather.com.cn/weather1d/101200503.shtml"
r = requests.get(url).content
soup = BeautifulSoup(r,"lxml")
title = soup.find('title')

print (r)
print (title)

