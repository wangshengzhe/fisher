# -*- coding: utf-8 -*-
from app.libs.httper import HTTP   # 导兄弟模块的类---》
from flask import current_app  # 指代当前的app 核心对象  也是一个代理


class YuShuBook:
    """
    组装url get访问api
    """
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"  # {} 里的参数是动态的    .format()
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"    # 类变量

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)            # json   对应dict
        self.__fill_single(result)

    def __fill_single(self, data):  # data是原始数据  result
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data["total"]
        self.books = data["books"]

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config["PER_PAGE"],
                                      self.calulate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def calulate_start(self, page):
        return (page-1) * current_app.config["PER_PAGE"]
