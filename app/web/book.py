# -*- coding: utf-8 -*-
from flask import jsonify, request, render_template, flash
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key  # 导 叔module 的函数名
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from .import web             # . 代表当前的包
import json


@web.route("/book/search")  # 使用蓝图来注册路由
def search():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()  # 从form中取参数
        page = form.page.data   # 因为form中有默认值，若果没有传入page参数，则取默认值
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)

        # return json.dumps(books, default=lambda o: o.__dict__)  #

    else:
        flash("搜索的关键字不符合要求，请重新输入关键字")
        # return jsonify(form.errors)  # 参数校验失败，form不报错
    return render_template("search_result.html", books=books)


@web.route("/book/<isbn>/detail")
def book_detail(isbn):
    pass



































@web.route("/test")
def test():
    r = {
        "name": 99,
        "age": 18,
        "score": 100
    }
    flash("hello ,wangshenge ")
    flash("hello , lovely")
    return render_template("test.html", data=r)

