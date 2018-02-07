# -*-coding:UTF-8-*-
# _author_= 'gao'


from AMS import Driver
from AMS.page import login

driver = Driver.driver("https://amsfe-test1.fishsaying.com")
login(driver,"admin","admin")
driver.quit()