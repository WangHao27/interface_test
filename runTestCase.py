# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：runTestCase.py
@Email：whang27@163.com
"""
import os
import sys
import time

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)


# 日志目录
LOG_DIR = os.path.join(BASE_DIR, "logs")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR, "reports")
# 测试用例目录
TESTCASES_DIR = os.path.join(BASE_DIR, "testcase/addressBook")

if __name__ == "__main__":
    print('开始运行脚本并生成测试报告文件'.center(40, '*'))
    os.system("pytest " + TESTCASES_DIR + " --alluredir=" + TEST_REPORT)
    print('脚本运行完毕'.center(47, '*'))
    time.sleep(3)
    print('开始生成测试报告'.center(45, '*'))
    os.system("allure generate " + TEST_REPORT + " -o " + TEST_REPORT + "\\html --clean")
    print('测试报告生成完毕'.center(45, '*'))
    os.system("allure open -h 127.0.0.1 -p 8090 " + TEST_REPORT)
