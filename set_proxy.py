#coding:utf-8

from selenium import webdriver
import time

#设置proxy访问IP138
PROXY = "113.66.147.83:9999"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

dr = webdriver.Chrome(chrome_options=chrome_options)
dr.maximize_window() #最大化chrome,访问url
url = 'http://www.ip138.com/'
dr.get(url)


print ("成功！")
time.sleep(20)
dr.close()
