# -*-coding:UTF-8-*-
# _author_= 'gao'
import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import Common
from common import configHttp as ConfigHttp
from common.Common import store

login_xls = Common.get_xls("test1.xlsx", "Sheet1")
# localReadConfig = readConfig.ReadConfig()
# configHttp = ConfigHttp.ConfigHttp()
# info = {}
# result_ = {}



@paramunittest.parametrized(*login_xls)
class Test(unittest.TestCase):
    result_ = {}
    localReadConfig = readConfig.ReadConfig()
    configHttp = ConfigHttp.ConfigHttp()
    results="pass"
    def setParameters(self, number, case_name, execute, method,domain, url, data, expect_result):
        self.number = number
        self.case_name = str(case_name)
        self.execute = execute
        self.method = str(method)
        self.domain = str(domain)
        self.url = str(url)
        self.body = data
        self.expect_result = expect_result
        self.return_json = None
        self.info = None


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
        # self.path = Log.get_result_path()
        print(self.case_name + "测试开始前准备")

    def testCase(self):
        """
        test body
        :return:
        """
        # set url

        self.configHttp.set_url(self.domain,self.url)
        self.logger.info("***********\t" + self.case_name + "\t***********")
        from common.Common import logger
        logger.info("第一步：设置url  " + str(self.url))
        if str.lower(self.method) == "post":
            # logger.info("self.body:" + self.body)
            params = eval(self.body)
            logger.info("第二步设置params:" + str(params))
            self.configHttp.set_data(params)
            logger.info("第三步：设置发送请求的参数:" + str(params))
            self.return_json = self.configHttp.post()

        elif str.lower(self.method) == "get":
            logger.info("第二步设置params:" + str(self.body))
            self.configHttp.set_params(str(self.body))
            logger.info("第三步：设置发送请求的参数:" + str(self.body))
            self.return_json = self.configHttp.get()

        # method = str(self.return_json.request)[
        #         int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
        logger.info(
            "第四步：发送请求" + ">>>>>>>>" + "请求方法：" + self.method.upper() + "\t return_json:" + str(self.return_json.json()))
        logger.info("响应时间:" + str(self.return_json.elapsed.microseconds/1000))
        # check result
        self.logger.info(self.expect_result)

        self.result_["t_id"] = self.number
        self.result_["t_name"] = self.case_name
        self.result_["t_method"] = self.method
        self.result_["t_url"] = self.url
        self.result_["t_param"] = self.body
        self.result_["t_hope"] = self.expect_result
        self.result_["t_actual"] = self.return_json.json()
        try:
            self.checkResult()
        except AssertionError:
            self.results="fail"
        self.result_["t_result"] = self.results
        self.logger.info("当前case测试结果")
        self.logger.info(self.result_)
        store(str(self.result_))
        self.logger.info("第五步：检查结果" + self.results)
        self.checkResult()
    def tearDown(self):
        """

        :return:
        """
        self.info = self.return_json
        # if info['code'] == 0:
        #     # get uer token
        #     token_u = Common.get_value_from_return_json(info, 'member', 'token')
        #     # set user token to config file
        #     localReadConfig.set_headers("TOKEN_U", token_u)
        # else:
        #     pass
        # self.log.build_case_line(self.case_name, self.info['code'], self.info['msg'])
        self.logger.info("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """

        if self.expect_result == "":
            pass
        else:
            expect_re = eval(self.expect_result)
            for expect in expect_re:
                # if self.return_json.json().get(expect) != expect_re.get(expect):
                    # self.results = "fail"
                    # self.logger.info("第五步：检查结果" + self.results)


                self.assertEqual(self.return_json.json().get(expect), expect_re.get(expect))

                # result = self.assertEquals(self.return_json.json().get(expect), expect_re.get(expect))
                # results = results.append(result)

                # try:
                #     self.assertEquals(self.return_json.json().get(expect), expect_re.get(expect))
                # except:
                #     self.logger.info("fail")
                # finally:
                #     self.logger.info("pass")
        # self.info = json.loads(self.return_json.text)
        # self.logger.info("act"+str(self.info.get("statuscode")))
        # self.logger.info("exp"+self.code)
        # self.assertEqual(str(self.info.get("statuscode")),self.code)
        # self.assertEqual(self.info.get("msg"),self.msg)
        # show return message
        # Common.show_return_msg(self.return_json)

        # if self.result == '0':
        #     email = Common.get_value_from_return_json(self.info, 'member', 'email')
        #     self.assertEqual(self.info['code'], self.code)
        #     self.assertEqual(self.info['msg'], self.msg)
        #     self.assertEqual(email, self.email)
        #
        # if self.result == '1':
        #     self.assertEqual(self.info['code'], self.code)
        #     self.assertEqual(self.info['msg'], self.msg)
