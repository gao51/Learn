# -*-coding:UTF-8-*-
# _author_= 'gao'
# coding=utf-8
import csv  # 导入csv 包
def parameter(path):
    list1 = []
    with open(path, "r") as csvfile:
        read = csv.reader(csvfile)
        # 循环输出每一行信息
        i = 0
        for user in read:
            i += 1
            if user[0] != "":
                del user[0]
                list1.append(user)
        csvfile.closed
    return list1

