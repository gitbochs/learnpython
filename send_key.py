#coding:utf-8
from selenium import webdriver
import time

dr = webdriver.Chrome()
#最大化chrome,访问url
dr.maximize_window()
url = 'http://www.google.com'
dr.get(url)

dr.find_element_by_id('lst-ib').send_keys("我爱我的祖国")
dr.find_element_by_name('btnK').click()

print ("成功！")
time.sleep(20)
dr.close()
