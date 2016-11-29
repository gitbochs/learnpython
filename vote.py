#coding:utf-8

from selenium import webdriver

dr = webdriver.Chrome()
#最大化chrome,访问url
dr.maximize_window()
url = 'http://www.google.com'
dr.get(url)

dr.find_element_by_id("hplogo").click()

print ("成功！")

dr.close()
