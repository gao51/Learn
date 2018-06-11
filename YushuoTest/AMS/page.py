# -*-coding:UTF-8-*-
# _author_= 'gao'
import time


def username(driver):
    driver1 = driver.find_element_by_class_name("fs-login-name")
    return driver1


def password(driver):
    return driver.find_element_by_class_name("fs-login-password")


def tips(driver):
    driver1 = driver.find_element_by_class_name("login-tips")
    return driver1


def button(driver):
    driver1 = driver.find_element_by_xpath("//*[@id=\"container\"]/div/div/div[5]/button")
    return driver1


def login(driver, username, password):
    # username(driver).clear()
    # password(driver).clear()
    driver.find_element_by_xpath("//*[@id=\"container\"]/div/div/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("//*[@id=\"container\"]/div/div/div[2]/input").send_keys(password)
    driver.find_element_by_xpath("//*[@id=\"container\"]/div/div/div[5]/button").click()
    time.sleep(1)
    return driver


