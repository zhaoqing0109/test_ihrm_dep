# 导包
import requests


# 创建员工的api类
class TestDepApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.dep_url = "http://ihrm-test.itheima.net" + "/api/company/department"

    # 封装添加部门的函数
    def add_dep(self, headers):
        response = requests.post(self.dep_url,
                                 json={"name": "牛牛",
                                       "code": "66666",
                                       "manager": "花花",
                                       "introduce": "部门介绍"},
                                 headers=headers)
        return response

    def query_dep(self, dep_id, headers):
        # 定义查询部门的url
        query_url = self.dep_url + "/" + dep_id
        # 发送查询部门的请求
        response = requests.get(query_url, headers=headers)
        return response

    def modify_dep(self, dep_id, headers, name):
        # 定义修改部门的url
        modify_url = self.dep_url + "/" + dep_id
        # 发送修改员工的请求
        response = requests.put(modify_url,
                                json={"name": name},
                                headers=headers)
        return response

    def del_dep(self, dep_id, headers):
        # 定义删除部门的url
        del_url = self.dep_url + "/" + dep_id
        # 发送删除部门的请求
        response = requests.delete(del_url, headers=headers)
        return response
