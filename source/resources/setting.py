# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：setting.py
@Email：whang27@163.com
"""

import os, sys

import redis

"""
文件路径配置
"""
BASE_DIR = os.path.dirname(os.path.dirname(__file__)).split('source')[0]
sys.path.append(BASE_DIR)

# 日志文件存放路径
TEST_LOG = os.path.join(BASE_DIR, "logs")
# testdata文件路径
TEST_DATA = os.path.join(BASE_DIR, "testdata")
# 测试报告数据
TEST_REPORT = os.path.join(BASE_DIR, "reports")
# 测试报告路径
TESTCASES_DIR = os.path.join(BASE_DIR, "reports/html")
# 应用配置文件路径
APPLICATION = os.path.join(BASE_DIR, "source/resources", "application.yaml")

# 通讯录测试数据
ADDRESSBOOK = os.path.join(TEST_DATA, "addressBook", "addressBook_test.yaml")




# 设置用于存储和读取接口临时数据的Redis连接池（备注：请自行修改数据库的值db，避免冲突）
def connect_redis():
    conn_pool = redis.ConnectionPool(host='127.0.0.1', password='westar@11', port=6379, db=3)
    re = redis.Redis(connection_pool=conn_pool)
    return re









if __name__ == '__main__':
    print(ADDRESSBOOK)