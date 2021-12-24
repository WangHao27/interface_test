# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：memberManagement.py
@Email：whang27@163.com
"""
import allure
from source.main.common.baseApi import BaseApi
from source.main.utils.fileUtils import FileUtils
from source.main.utils.loggers import logger
from source.resources import setting


class MemberManageApi(BaseApi):
    """
    通讯录成员管理相关接口
    """
    log = logger

    def __init__(self):
        """
        继承基类初始化方法，获取通讯录管理token
        :param corpsecret: 通讯录的凭证密钥
        """
        super().__init__()
        corpsecret = FileUtils(setting.APPLICATION).read()['enterprise']['applets_key']['address_book']
        self.s.params = {'access_token': self.get_token(corpsecret)}

    @allure.step("读取成员信息")
    def get_member(self, user_id):
        """
        请求方式：GET（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :param user_id: 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节
        :return:
        """
        self.log.info("读取成员信息 >>>>>")
        get_member_url = f'{self.base_url}/user/get'
        r = self.send("get", get_member_url, userid=user_id)
        return r

    @allure.step("更新成员信息")
    def update_member(self, user_id, name, mobile):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :param user_id: 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节
        :param name: 成员名称。长度为1~64个utf8字符
        :param mobile: 手机号码。企业内必须唯一。
        :return:
        """
        self.log.info("更新成员信息 >>>>>")
        update_member_url = f'{self.base_url}/user/update'
        r = self.send("post", url=update_member_url, userid=user_id, name=name, mobile=mobile)
        return r

    @allure.step("创建成员信息")
    def create_member(self, user_id, name, mobile, department):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :param user_id: 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节。
                        只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。
        :param name: 成员名称。长度为1~64个utf8字符
        :param mobile: 手机号码。企业内必须唯一，mobile/email二者不能同时为空
        :param department: 成员所属部门id列表,不超过100个
        :return:
        """
        self.log.info("创建成员信息 >>>>>")
        create_member_url = f'{self.base_url}/user/create'
        r = self.send("post", url=create_member_url, userid=user_id, name=name, mobile=mobile, department=department)
        return r

    @allure.step("删除成员信息")
    def delete_member(self, user_id):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :param user_id: 成员UserID。对应管理端的帐号
        :return:
        """
        self.log.info("删除成员信息 >>>>>")
        delete_member_url = f'{self.base_url}/user/delete'
        r = self.send("get", delete_member_url, userid=user_id)
        return r


member_manage_api = MemberManageApi()
