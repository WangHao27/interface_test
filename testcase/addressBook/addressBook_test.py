# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：addressBook_test.py
@Email：whang27@163.com
"""

import os
import allure
import pytest
from source.main.api.addressBook.memberManagement import MemberManageApi
from source.main.common.testBaseCase import TestBaseCase
from source.main.utils.assertUtils import AssertUtils
from source.main.utils.fileUtils import FileUtils
from source.main.utils.loggers import logger
from source.resources import setting

# 测试数据路径
test_address_dir = os.path.join(setting.TEST_DATA, "addressBook", "addressBook_test.yaml")
addressPath = FileUtils(test_address_dir).read()

@allure.feature("成员管理模块接口测试")
class TestAddress(TestBaseCase):
    log = logger

    def setup(self):
        """
        实例化MemberManageApi()类
        :return:
        """

        self.member_manage_api = MemberManageApi()

    @allure.story("获取成员信息测试用例")
    @pytest.mark.parametrize("user_id", addressPath['test_get_member'])
    def test_get_member(self, user_id):
        r = self.member_manage_api.get_member(user_id)
        AssertUtils(r).equal('userid', user_id[0])


    # @allure.story("新增成员信息测试用例")
    # @pytest.mark.parametrize("user_id, name, mobile, department", addressPath['test_create_member'])
    # def test_create_member(self, user_id, name, mobile, department):
    #     r = self.member_manage_api.create_member(user_id, name, mobile, department)
    #     AssertUtils(r).equal('errcode', '0')

    @allure.story("修改成员信息测试用例")
    @pytest.mark.parametrize("user_id, name, mobile", addressPath['test_update_member'])
    def test_update_member(self, user_id, name, mobile):
        r = self.member_manage_api.update_member(user_id, name, mobile)
        AssertUtils(r).equal('errcode', 0)

    # @allure.story("删除成员信息测试用例")
    # @pytest.mark.parametrize("user_id", addressPath['test_delete_member'])
    # def test_delete_member(self, user_id):
    #     self.member_manage_api.delete_member(user_id)







if __name__ == '__main__':
    test_address_dir = os.path.join(setting.TEST_DATA, "addressBook", "addressBook_test.yaml")
    print(test_address_dir)