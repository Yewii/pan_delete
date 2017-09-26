#-*-coding:utf8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import requests
import os

def judge(urlstr):
    driver.get(urlstr)
    l = r'<a class="usjjQDB6" href="javascript:void(0);" title="(.*?)">'
    pattern = re.compile(l, re.U)
    iteam = re.findall(pattern, page)
    if iteam=='':
        print('1')
    else:
        print('0')
    return


def listloop():
    m = r'<a class="usjjQDB6" href="javascript:void(0);" title="(.*?)">'
    pattern1 = re.compile(m, re.U)  # 编译正则表达式
    iteamnew = re.findall(pattern1, page)
    return iteamnew

#打开浏览器
driver = webdriver.Firefox()
driver.get('https://pan.baidu.com/')

#登录
driver.find_element_by_xpath(".//*[@id='login-middle']/div/div[6]/div[2]/a").click()
driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_4__userName']").send_keys("yywzh424")
driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_4__password']").send_keys("1997424yywzh*")
driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_4__submit']").click()

#等待
time.sleep(10)

#获取当前页面源代码
f=open('page_html.txt','w')
page = driver.page_source#获取当前页面源代码
f.write(page)


#获取当前文件夹下目录
p = r'class="usjjQDB6" title="(.*?)">'
pattern2 = re.compile(p,re.U)#编译正则表达式
iteam=re.findall(pattern2,page)
print(iteam)
length=len(iteam)
print(length)

#打印当前页面内容
# print('************************')
# data = driver.find_element_by_xpath("html").text
# print(data)

#循环建立目录
for i in range(length):
    urlll='https://pan.baidu.com/disk/home?#list/vmode=grid&path=%2F'+iteam[i]
    print(urlll)
    driver.get(urlll)

    # i=judge(url)
    # print(judge(url))
    # if i==1:
    #     print('1')
    # else:
    #     print('0')
    judge('urlll')

print('ok')



