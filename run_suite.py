# 导包
import unittest
import HTMLTestRunner_PY3
import app

# 创建测试套件
from script.ihrm_dep import TestIHRMDeployee

suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMDeployee))
# 定义测试报告的名称
report_name = app.BASE_DIR + "/report/ihrm.html"
# 使用HTMLTestRunner_PY3生成测试报告
with open(report_name, 'wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=2,title="IHRM接口测试报告", description="这是IHRM部门增删改查的测试报告")
    # 使用runner运行测试套件
    runner.run(suite)