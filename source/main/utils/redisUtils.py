# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：redisUtils.py
@Email：whang27@163.com
"""

import json
from source.main.utils.loggers import logger
from source.resources import setting


class RedisUtils:
    """
    redis写入与读取封装工具类，数据获取请使用debugtalk中的get_dataFromRedis(key)方法
    """
    log = logger

    def __init__(self):
        """
        初始化连接
        """
        try:
            self.r = setting.connect_redis()
            # 设置数据过期时间默认为24小时
            self.expire = 864000
        except Exception as e:
            self.log.error("redis连接失败,错误信息为%s" % e)

    def get(self, key):
        """
        获取key的值并转换格式
        :param key:
        :return:
        """
        if self.r.exists(key):
            res = self.r.get(key)
            return res.decode('utf8')
        else:
            self.log.error(f"{key} 不存在！")

    def ttl(self, key):
        """
        获取key的过期时间
        :param key:
        :return:
        """
        if self.r.exists(key):
            return self.r.ttl(key)
        else:
            self.log.error(f"{key} 不存在！")

    def set(self, key, value):
        """
        向redis中写入临时数据，为单个键值对
        value的值可以是列表或字典
        :param key:
        :param value:
        :return:
        """
        # value值为列表或字典时进行json序列化
        if type(value) in (list, dict):
            new_val = json.dumps(value, ensure_ascii=False)
            self.r.set(key, new_val, self.expire)
        else:
            self.r.set(key, value, self.expire)

    def set_list(self, data_list):
        """
        向redis中写入列表嵌套字典类型：
         example_1 ：[{key:val, key:val}]
         example_2： [{key: {key1:val1}, key2: [val2]}]
        :param list:
        :return:
        """
        if isinstance(data_list, list):
            for dic in data_list:
                for key, val in dic.items():
                    if type(val) in (dict, list):
                        new_val = json.dumps(val, ensure_ascii=False)
                        self.r.set(key, new_val, self.expire)
                    else:
                        self.r.set(key, val, self.expire)
        else:
            self.log.error("数据非列表嵌套字典类型，无法写入！")

    def add(self, key, value):
        """
        向Reids中追加数据，保留原有数据
        :param key:
        :param value:
        :return:
        """
        self.r.sadd(key, value)

    def get_members(self, key):
        """
        通过add方法写入的数据，使用本方法读取，bytes类型数据需反编译(decode)为str
        :param key:
        :return:
        """
        if self.r.exists(key):
            res = self.r.smembers(key)
            return res
        else:
            self.log.error(f"{key} 不存在！")


# 实例化
RedisUtils = RedisUtils()