# 导包
import requests


# 创建登录api测试类
class TestLoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.dep_url = "http://ihrm-test.itheima.net" + "/api/company/department"

    # 创建登录的函数
    def login(self, jsonData, headers):
        response = requests.post(url=self.login_url,
                                 json=jsonData,
                                 headers=headers)
        return response
