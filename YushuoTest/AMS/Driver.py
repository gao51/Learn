# -*-coding:UTF-8-*-
# _author_= 'gao'
import os
from selenium import webdriver


def driver(url=None):
    driver = webdriver.Chrome(os.getcwd() + "\\File\\chromedriver.exe")
    if url is None:
        pass
    else:
        driver.get(url)
    return driver
