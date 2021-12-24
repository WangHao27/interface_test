# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：conftest.py
@Email：whang27@163.com
"""
import time
import pytest

"""
fixture作用范围：
scope = session，所有测试.py文件执行前执行一次
scope = module，每一个测试.py文件执行前都会执行一次
scope = class，每一个测试文件中的测试类执行前都会执行一次
scope = function，所有文件的测试用例执行前都会执行一次
"""

@pytest.fixture(scope='function')
def getTime():
    millis = str(round(time.time() * 1000))
    return millis