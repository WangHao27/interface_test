# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：testBaseCase.py
@Email：whang27@163.com
"""
from source.main.utils.loggers import logger


class TestBaseCase:
    """
    测试用例的基类，被所有用例继承
    """
    log = logger

    def setup(self):
        """
        单个用例执行前的操作
        :return:
        """
        self.log.info("=======================================Start Test========================================")

    @classmethod
    def setup_class(cls):
        """
        所有用例执行前的操作
        :return:
        """
        cls.log.info("======================================Start TestCase======================================")

    def teardown(self):
        """
        单个用例执行后的操作
        :return:
        """
        self.log.info("========================================End Test======================================== \n")

    @classmethod
    def teardown_class(cls):
        """
        所有用例执行后的操作
        :return:
        """
        cls.log.info("======================================End TestCase====================================== \n")