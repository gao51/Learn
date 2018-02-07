from common.configHttp import localReadConfig


class BaseApi:
    port = localReadConfig.get_http("port")
    timeout = localReadConfig.get_http("timeout")
    def __init__(self):
        pass
    def url(self,ServerName,InterfaceName):
        host = localReadConfig.get_http(ServerName)
        if self.port != "":
            url = host+InterfaceName
        else:
            url = host+":"+self.port+InterfaceName
        return url