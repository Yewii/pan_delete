#-*-coding:utf8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import requests
import os

driver = webdriver.Firefox()
url='https://pan.baidu.com/'
driver.get(url)

driver.find_element_by_xpath(".//*[@id='login-middle']/div/div[6]/div[2]/a").click()
driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_4__userName']").send_keys("yywzh424")
driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_4__password']").send_keys("1997424yywzh*")
driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_4__submit']").click()

time.sleep(5)


#获取当前url
url = driver.current_url
print('当前页面url'+url)

f=open('page_html.txt','w')


page = driver.page_source#获取当前页面源代码
# print(page)
f.write(page)

#获取当前文件夹下目录
p = r'class="asbfGB3b" title="(.*?)">'
pattern1 = re.compile(p,re.U)#我们在编译这段正则表达式
# matcher1 = re.match(pattern1,page,re.S)#在源文本中搜索符合正则表达式的部分
iteam=re.findall(pattern1,page)#打印出来
print(iteam)
print(len(iteam))

#打印当前页面内容
# print('************************')
# data = driver.find_element_by_xpath("html").text
# print(data)

#判断传入字符串是否包含中文
def contain_zh(word):
    word = word.decode()
    global zh_pattern
    match = zh_pattern.search(word)
    return match




