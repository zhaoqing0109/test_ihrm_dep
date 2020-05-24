# 导包
import unittest
import logging
import requests
from api.dep_api import TestDepApi
from api.login_api import TestLoginApi
from utils import assert_common


# 创建测试类、集成unittest.TestCase


class TestIHRMDeployee(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"
        self.dep_api = TestDepApi()  # 部门实例化
        self.login_api = TestLoginApi()  # 登录实例化

    def tearDown(self):
        pass

    # 创建测试部门增删改查的函数
    def test_dep(self):
        # 登录
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印登录的数据
        logging.info("登录的结果为：{}".format(response.json()))
        # 提取令牌
        token = response.json().get("data")
        # 保存令牌到请求头当中
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        # 打印令牌
        logging.info("请求头中令牌：{}".format(headers))

        # 添加部门
        response = self.dep_api.add_dep(headers)
        # 打印添加的结果
        logging.info("添加部门的结果为:{}".format(response.json()))
        # 提取添加部门中的id
        dep_id = response.json().get("data").get("id")
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

        # 查询部门
        # 发送查询部门的请求
        response = self.dep_api.query_dep(dep_id, headers)
        logging.info("查询部门的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

        # 修改部门
        # 发送修改部门的请求
        response = self.dep_api.modify_dep(dep_id, headers, "妞妞")
        # 打印修改的结果
        logging.info("修改部门的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

        # 删除部门
        # 发送删除部门的请求
        response = self.dep_api.del_dep(dep_id, headers)
        # 打印删除的结果
        logging.info("删除部门的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)
