# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(os.path.dirname(os.getcwd()) + "\\File\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://mp-test1.cpmap.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # def test_login(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     #driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/input").clear()
    #     driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/input").send_keys("adcb")
    #     #driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/input").clear()
    #     driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/input").send_keys("123456")
    #     driver.find_element_by_class_name("login-btn").click()
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenuim")
        driver.find_element_by_id("form").submit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors);


if __name__ == "__main__":
    unittest.main()
