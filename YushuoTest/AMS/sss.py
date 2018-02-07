# # # # -*-coding:UTF-8-*-
# # # # _author_= 'gao'
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(30)
# driver.set_window_size(100, 50)
#
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("Selenium2")
# driver.find_element_by_id("su").text
# # # #driver.quit()

# # import os
# #
# # for x in 'abcdefg':
# #     print(x, end=' ')
# # i = 0
# # while i < 11:
# #     # print(i, ' is smaller than 3')
# #     path = "I:\\aa\\" + str(i) + ".txt"
# #     # print(path)
# #     f = open(path, "w")
# #     f.close()
# #     os.remove(path)
# #     i += 1
# #
# # for i in range(100):
# #     if i % 2 == 0:
# #         print(i)
# f = ['x', 'y', 'z']
# # f[0:0] = 'a'
# f.insert(0, 'b')
# print(f)
# f.remove('x')
# print(f)
# f[1] = 'w'
# print(f)
# del f[1:2]
# print(f)
#
# name = {"小明": 19, "小强": 20}
# print(name.get("小明"))
# a = [1, 2, 3, 4, 5]
# b = ['a', 'b', 'c', 'd', 'e']
# for a, b in zip(a, b):
#     print(a, b)
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# for letter, num in enumerate(letters):
#     print(num, 'is', letter + 1)
# import jieba
# seg_list = jieba.cut_for_search("三顾茅庐", HMM=False)  # 搜索引擎模式
# print(", ".join(seg_list))

#
# list = [1,2,3,4]
# it = iter(list)
# print(next(it))
# print(next(it))
# import os
#
#
# class a:
#     def __init__(self, x, y):
#         self.c = x
#         self.b = y
#
#
# d = a(8, 9)
# print(d.c)
#
# print(os.getcwd())
# os.chdir('d://')
# print(os.getcwd())


import unittest

def div(a,b):
    return a-b


class DivTest(unittest.TestCase):
    def test_div_001(self):
        self.assertEqual(div(3,2),1)

    def test_div_002(self):
        self.assertEqual(div(3,3),0)

    def test_div_003(self):
        self.assertEqual(div(2, 3), -1)