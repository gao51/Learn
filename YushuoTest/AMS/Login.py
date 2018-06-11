# -*-coding:UTF-8-*-
# _author_= 'gao'
import datetime
import time

import os

import sys
from selenium import webdriver

#
# driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

# print(os.getcwd())
# list = ReadCSV.parameter(os.getcwd()+"\\paramet\\test.csv")
# i = 0
# for list1 in list:
#     driver = Driver.driver()
#     driver.get(url)
#     login(driver, list1[0], list1[1])
#     print("第", i + 1, "次登陆>>>>>>用户名为：" + list1[0], '\t', "密码为：", list1[1])
#     if driver.current_url == "https://amsfe-test1.fishsaying.com/login":
#         print(page.tips(driver).text)
#     elif driver.current_url == "https://amsfe-test1.fishsaying.com/":
#         print("登陆成功")
#     i += 1
#     driver.quit()
driver = Driver.driver(url)
# driver = driver.get(url)
login(driver, 'admin', 'admin')
# 图文审核
driver.get('https://amsfe-test1.fishsaying.com/cultureNumber-pa-audit')
# try:
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                 '//*[@id="container"]/div/div[2]/div/div/ul/li[2]/dt[8]/span[1]')))
time.sleep(1)
driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div/ul/li[2]/dt[8]/span[2]').click()

WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,'fs-modal-header')))

driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/button[1]').click()
# except Exception as e:
#     print(e)
