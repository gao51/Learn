# -*-coding:UTF-8-*-
# _author_= 'gao'
import datetime
import time

import os
from selenium import webdriver

#
# driver = webdriver.Chrome()
from AMS import Driver, ReadCSV
from AMS import page
from AMS.page import login

url = "https://amsfe-test1.fishsaying.com"

# driver = Driver.driver()
# driver.get(url)
# login(driver, "admin", "admin")
# if driver.current_url == "https://amsfe-test1.fishsaying.com/login":
#     print(page.tips(driver).text)
# elif driver.current_url == "https://amsfe-test1.fishsaying.com/":
#     print("登陆成功")
# driver.quit()
print(os.getcwd())
list = ReadCSV.parameter(os.getcwd()+"\\paramet\\test.csv")
i = 0
for list1 in list:
    driver = Driver.driver()
    driver.get(url)
    login(driver, list1[0], list1[1])
    print("第", i + 1, "次登陆>>>>>>用户名为：" + list1[0], '\t', "密码为：", list1[1])
    if driver.current_url == "https://amsfe-test1.fishsaying.com/login":
        print(page.tips(driver).text)
    elif driver.current_url == "https://amsfe-test1.fishsaying.com/":
        print("登陆成功")
    i += 1
    driver.quit()
