#coding:utf-8

from selenium import webdriver
import time

dr = webdriver.Chrome()
time.sleep(2)
print ("最大化chrome,访问url")

url = 'http://www.baidu.com'
dr.maximize_window()
dr.get(url)

time.sleep(2)
print ("关闭chrome")

#dr.close()
