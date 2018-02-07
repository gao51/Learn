import unittest

import selenium
import time

import unittest2
from selenium import webdriver


# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("https://test1-cp.cpmap.com")
#
# s = driver.find_elements_by_class_name("login-input")
#
# driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div[1]/input").send_keys("adcb")
# driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div[2]/input").send_keys("123456")
# driver.find_element_by_class_name("login-btn").click()
# time.sleep(3)
#
# # driver.add_cookie({'name':'xxxxx','value':'yyyyyy'})
# cookies = driver.get_cookies()
# for cookie in driver.get_cookies():
#     print("%s -> %s" % (cookie['name'], cookie['value']))

# text = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/div[2]").text
# print(text)
# x = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/div[2]")
#
# webdriver.ActionChains(driver).move_to_element(x).perform()
# time.sleep(3)
# y = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/div[2]/div[2]/a").text
# print(y)
# webdriver.ActionChains(driver).click(y).perform()


class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.baseurl = "https://mp-test1.cpmap.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.baseurl)
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/input").send_keys("adcb")
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/input").send_keys("123456")
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/a").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors);


if __name__ == "__main__":
    unittest.main()
