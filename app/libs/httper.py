# -*- coding: utf-8 -*-
import requests


class HTTP:
    """

    """
    @staticmethod
    def get(url, return_json=True):  #
        r = requests.get(url)   # get请求
        print("r = requests.get(url)中r的类型：", end="---->")
        print(type(r))
        if r.status_code != 200:
            return {} if return_json else ""  # 三元表达式
        return r.json() if return_json else r.text  # 200 ： json字符串r.json()，或者普通字符串r.text




