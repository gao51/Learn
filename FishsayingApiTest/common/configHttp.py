# -*-coding:UTF-8-*-
# _author_= 'gao'

import requests
import json

from bottle import basestring
from requests import Timeout
from urllib3.exceptions import ReadTimeoutError

import readConfig
from common.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()
def amscookies():
    amsurl = "https://ams-test1.fishsaying.com/a/login?new=1"
    data = {"username": "admin", "password": "admin"}
    return requests.post(amsurl, data=data).cookies

def capicookies():
    amsurl = "https://login-test1.fishsaying.com/webapi/login2"
    data = {"username": "test121801", "password": "123456"}
    return requests.post(amsurl, data=data).cookies
def strlist(data):
    data = data.split("||")
    list = []
    for i in range(len(data)):
        dict = eval(data[i])
        print(dict)
        list.append(dict)
        print(list)
    return list

amscook = amscookies()
capicook = capicookies()


class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("amsurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.cookies=""
        self.data = {}
        self.url = None
        self.files = {}
        self.body = None
        self.json=[]

    def is_tring(self, anobj):
        return isinstance(anobj, basestring)

    def set_url(self,domain, url):
        if domain !="-":
            host = localReadConfig.get_http(domain+"url")
        elif domain == "-":
            host = ""
        if port =="":
            self.url = host + url
            self.logger.info(self.url)
        else:
            self.url = host + ":" + port + url
            self.logger.info(self.url)

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_json(self, data):
        self.json = data

    def set_body(self, body):
        if (self.is_tring(body)):
            body = json.loads(body)
            body = json.dumps(body)
            self.body = body
        else:
            self.body = body

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        self.logger.error("begining")
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers,cookies = self.cookies, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None
        except Timeout:
            self.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        # self.logger.info('self.body' + str(type(self.body)))
        # self.logger.info('self.data' + str(type(self.data)))
        try:
            #self.logger.info("开始调接口：")
            response = requests.post(self.url, headers=self.headers,cookies = self.cookies, data=self.data, json=self.body, files=self.files,
                                     timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            # self.logger.info("time out")
            self.logger.error("Time out!")
            return None
        except Timeout:
            self.logger.error("Time out!")
            return None

    def delete(self):
        # self.logger.info('self.body' + str(type(self.body)))
        # self.logger.info('self.data' + str(type(self.data)))
        try:
            # self.logger.info("开始调接口：")
            response = requests.delete(self.url, headers=self.headers, cookies=self.cookies, params=self.params,
                                        files=self.files,
                                       timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            # self.logger.info("time out")
            self.logger.error("Time out!")
            return None
        except Timeout:
            self.logger.error("Time out!")
            return None

    def put(self):
        # self.logger.info('self.body' + str(type(self.body)))
        # self.logger.info('self.data' + str(type(self.data)))
        try:
            # self.logger.info("开始调接口：")
            response = requests.put(self.url, headers=self.headers, cookies=self.cookies, json=self.json,
                                        files=self.files,
                                       timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            # self.logger.info("time out")
            self.logger.error("Time out!")
            return None
        except Timeout:
            self.logger.error("Time out!")
            return None
    def set_cookies(self,domain):
        if domain=="ams":
            self.cookies = amscook
        elif domain == "capi":
            self.cookies = capicook

