# -*-coding:UTF-8-*-
# _author_= 'gao'
import unittest

import requests
import time

import readConfig as readConfig
from common import Log as Log, configHttp
from common import Common
from common import configHttp as ConfigHttp
from common.Common import logger, replacebody
from common.Common import store




class Base(unittest.TestCase):
    result_ = {}
    localReadConfig = readConfig.ReadConfig()
    configHttp = ConfigHttp.ConfigHttp()
    results = "pass"
    url = ""
    number = ""
    case_name = ""
    execute = ""
    method = ""
    body = ""
    expect_result = ""
    domain = ""
    return_json = None
    amscookies = ConfigHttp.amscookies


    def setParameters(self, number, case_name, execute, method, domain, url, data, expect_result):
        self.number = number
        self.case_name = str(case_name)
        self.execute = execute
        self.method = str(method)
        self.domain = str(domain)
        self.url = str(url)
        self.body = replacebody(data)
        self.expect_result = expect_result


    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.logger.info("***********\t" + self.case_name + "\t***********")

    # def testCase(self):
    #     """
    #     test body
    #     :return:
    #     """
    #     pass


    def conserve(self):
        self.result_["t_id"] = self.number
        self.result_["t_name"] = self.case_name
        self.result_["t_method"] = self.method.upper()
        self.result_["t_url"] = self.url
        self.result_["t_param"] = self.body
        self.result_["t_hope"] = self.expect_result
        self.result_["t_actual"] = self.return_json.json()
        try:
            self.checkResult()
        except AssertionError:
            self.results = "fail"
        self.result_["t_result"] = self.results
        store(str(self.result_))



    def tearDown(self):
        """
        :return:
        """
        self.logger.info("测试结束，输出log完结\n\n")



    def checkResult(self):
        """
        check test result
        :return:
        """
        if self.return_json.status_code == 500:
            self.results = "Erro"
            self.assertNotEqual(self.return_json.status_code,500)
        elif self.expect_result == "" :
            pass
        elif self.expect_result[0]=="{":
            expect_re = eval(self.expect_result)
            for expect in expect_re:
                self.assertEqual(self.return_json.json().get(expect), expect_re.get(expect))
        else:
            self.assertIn(self.expect_result,str(self.return_json.text))
