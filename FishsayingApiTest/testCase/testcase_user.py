

import paramunittest
from common import Common
from common.BaseCase import Base
from common.configHttp import strlist

login_xls = Common.get_xls("test1.xlsx", "用户管理")


@paramunittest.parametrized(*login_xls)
class Test(Base):
    def testCase(self):
        # 设置url
        self.configHttp.set_url(self.domain,self.url)
        # 设置cookies
        self.configHttp.set_cookies(self.domain)
        from common.Common import logger
        logger.info("第一步：设置url  " + str(self.url))
        if str.lower(self.method) == "post":
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
        elif str.lower(self.method) == "delete":
            logger.info("第二步设置params:" + str(self.body))
            self.configHttp.set_params(str(self.body))
            logger.info("第三步：设置发送请求的参数:" + str(self.body))
            self.return_json = self.configHttp.delete()
        elif str.lower(self.method) == "put":
            logger.info("第二步设置params:" + str(self.body))
            self.configHttp.set_json(strlist(self.body))
            logger.info("第三步：设置发送请求的参数:" + str(strlist(self.body)))
            self.return_json = self.configHttp.put()
        logger.info(
            "第四步：发送请求" + "->" + "请求方法：" + self.method.upper() + "\t 返回结果:" + str(self.return_json.json()))
        self.amscookies = self.return_json.cookies
        logger.info("响应时间:" + str(self.return_json.elapsed.microseconds/1000))
        logger.info("期望结果："+self.expect_result)
        self.conserve()
        logger.info("第五步：检查结果" + self.results)
        self.checkResult()
