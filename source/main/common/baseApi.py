# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：baseApi.py
@Email：whang27@163.com
"""

import allure
import requests
from source.main.utils.fileUtils import FileUtils
from source.main.utils.loggers import logger
from source.resources import setting


class BaseApi:
    """
    接口基类，用于被其它接口继承
    """
    log = logger

    def __init__(self):
        """
        实例化Session(),初始化基础URL
        """
        self.s = requests.Session()
        self.base_url = FileUtils(setting.APPLICATION).read()['api']['base_url']

    @allure.step("获取应用凭证")
    def get_token(self, corpsecret):
        """
        请求方式：GET（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :param corpid: 企业ID，每个企业都拥有唯一的corpid
        :param corpsecret: 小程序的凭证密钥(不同小程序密钥不同)
        :return
        """
        corpid = FileUtils(setting.APPLICATION).read()['enterprise']['corpId']
        r = requests.get(
            f'{self.base_url}/gettoken?corpid={corpid}&corpsecret={corpsecret}')
        token = r.json()['access_token']
        return token

    def send(self, method, url, **kwargs):
        """
        对传入的请求分类，调用不同的请求方式，作基本的异常处理操作
        :param method: 接口请求方式
        :param url: 请求URL
        :param kwargs: 请求参数
        :return:
        """
        self.log.info("*********************************request details*********************************")
        result = ""
        try:
            if method == 'get':
                result = self.s.request('GET', url, params=kwargs)
                self.log.info(f"Method    ：GET")
            if method == 'post':
                result = self.s.request('POST', url, json=kwargs)
                self.log.info(f"Method    ：POST")
            if method == 'put':
                result = self.s.request('PUT', url, data=kwargs)
                self.log.info(f"Method    ：PUT")

            self.log.info(f"URL       ：{result.url}")
            self.log.info(f"Params    ：{kwargs}")
            self.log.info(f"Headers   : {result.headers} \n")
        except Exception as e:
            self.log.error(f"{method}请求错误：{e}")
            return e
        if result.status_code in range(400, 501):
            code = result.status_code
            self.log.error(f"{method}请求错误，响应码：{code}")
        else:
            self.log.info("*********************************response details*********************************")
            self.log.info(f"status_code: {result.status_code}")
            result = result.json()
            self.log.info(f"Response   : {result} \n")
            return result
