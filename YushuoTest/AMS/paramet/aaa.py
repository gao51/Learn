# -*-coding:UTF-8-*-
# _author_= 'gao'
# for x in 'abcdefg':
#     print(x, end='>')
# print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         if i+1>2 and j>1:
#             print('|  '+'{}×{}={}'.format(i, j, i * j), end=' \t')
#         else:
#             print('{}×{}={}'.format(i, j, i * j), end=' \t')
#     print()
# import requests
#
# r = requests.get(url='https://restapi-test1.fishsaying.com/api/mp/v1/culturalpoint/aiUserCount',
#                  params={'userId': '65f4f8811b864b60bd6919063920f41e'})  # 最基本的GET请求
# print(r.text)  # 获取返回状态


# r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的GET请求
# print(r.url)
# print(r.text)
import requests


class api():
    def GET( url, params):
        r = requests.get(url=url,params=params)  # 最基本的GET请求
        return r.text


x =api.GET('https://restapi-test1.fishsaying.com/api/mp/v1/culturalpoint/aiUserCount',
           '''{'userId':'65f4f8811b864b60bd6919063920f41e'}''')
print(x)