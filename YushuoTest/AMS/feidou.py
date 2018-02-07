# -*-coding:UTF-8-*-
# _author_= 'gao'
import random
import time
from selenium import webdriver

from AMS import ReadCSV

# driver = webdriver.Chrome()
# driver.get("http://admin-test.feedou.net/login")
# driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/input").send_keys("数据测试")
# driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/input").send_keys("123456")
# driver.find_element_by_class_name("login-btn").click()
# time.sleep(3)
# print(driver.current_url)
# if driver.current_url == "http://admin-test.feedou.net/login":
#     print("登录失败")
#     print(driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[3]/span").text)
# elif driver.current_url == "http://admin-test.feedou.net/":
#     print("登陆成功")

list = ReadCSV.parameter("C:\\Users\\gao\\Desktop\\test.csv")
i = 0
pwd = ""
driver = webdriver.Chrome()
driver.get("http://admin-test.feedou.net/login")
for list1 in list:
    for j in range(random.randint(6, 12)):
        pwd = pwd + str(chr(random.randint(97, 122)))
    # pwd = pwd + str(random.randint(0, 9))
    # pwd = "rzivdvgp"
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/input").clear()
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/input").send_keys(list1[0])
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/input").clear()
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/input").send_keys(pwd)
    driver.find_element_by_class_name("login-btn").click()
    print("第" + str(i + 1) + "次登陆>>>>>>用户名为：" + list1[0] + '\t\t' + "密码为：" + pwd + '\t\t', end=' ')
    pwd = ""
    time.sleep(3)
    i += 1
    if driver.current_url == "http://admin-test.feedou.net/login":
        print("登录失败", end=' ')
        if driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[3]/span").text == "请输入正确验证码！":
            print(driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[3]/span").text, end=' ')
            print("!!!!!!!!!!!!")
        else:
            print(driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[3]/span").text)
    elif driver.current_url == "http://admin-test.feedou.net/":
        print("登陆成功")
        # driver.quit()
