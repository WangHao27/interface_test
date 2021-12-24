# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：assertUtils.py
@Email：whang27@163.com
"""
import jsonpath

from source.main.utils.loggers import logger


class AssertUtils:
    """
    结果断言类
    """
    log = logger

    def __init__(self, result):
        self.result = result
        if self.result is None:
            self.log.error("结果数据为空！")

    def equal(self, valuePath, expectValue):
        """
        实际结果等于预期结果
        :return:
        """
        if valuePath is None or expectValue is None:
            self.log.error("结果路径或预期值为空！")

        # 通过jsonPath获取实际结果
        actualValue = jsonpath.jsonpath(self.result, f'$..{valuePath}')[0]
        if actualValue == expectValue:
            self.log.info(f"assert {valuePath} equal {expectValue} ==> pass")
        else:
            self.log.warning(f"assert {valuePath} equal {expectValue} ==> fail")
            self.log.info(f"actual_value : {actualValue}")

    def contains(self, valuePath, expectValue):
        """
        实际结果包含预期结果
        :return:
        """
        if valuePath is None or expectValue is None:
            self.log.error("结果路径或预期值为空！")

        actualValue = jsonpath.jsonpath(self.result, f'$..{valuePath}')[0]
        if expectValue in actualValue:
            self.log.info(f"assert {valuePath} contains {expectValue} ==> pass")
        else:
            self.log.info(f"assert {valuePath} contains {expectValue} ==> fail")
            self.log.info(f"actual_value : {actualValue}")

    def contained_by(self, valuePath, expectValue):
        """
        预期结果包含实际结果
        :return:
        """
        if valuePath is None or expectValue is None:
            self.log.error("结果路径或预期值为空！")

        actualValue = jsonpath.jsonpath(self.result, f'$..{valuePath}')[0]
        if actualValue in expectValue:
            self.log.info(f"assert {valuePath} contained_by {expectValue} ==> pass")
        else:
            self.log.info(f"assert {valuePath} contained_by {expectValue} ==> fail")
            self.log.info(f"actual_value : {actualValue}")


    def length_equal(self, valuePath, expectValue):
        """
        实际结果和预期结果字段长度一样
        :return:
        """
        if valuePath is None or expectValue is None:
            self.log.error("结果路径或预期值为空！")

        actualValue = jsonpath.jsonpath(self.result, f'$..{valuePath}')[0]
        if len(actualValue) == len(expectValue):
            self.log.info(f"assert {valuePath} length_equal {expectValue} ==> pass")
        else:
            self.log.info(f"assert {valuePath} length_equal {expectValue} ==> fail")
            self.log.info(f"actual_value : {actualValue}")

