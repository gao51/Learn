# -*-coding:UTF-8-*-
# _author_= 'gao'
from AMS import Login, Driver

driver = Driver.driver("https://amsfe-test1.fishsaying.com")
Login.login(driver,"admin","admin")
