""""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author: 王圣哲
date:   2019/3/15
Description:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


class BookViewModel:
    def __init__(self, book):
        self.title = book["title"]
        self.publisher = book['publisher']
        self.author = '、'.join(book["author"])
        self.image = book["image"]
        self.price = book["price"]
        self.summary = book["summary"]
        self.pages = book["pages"]


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

















class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            "book": [],
            "total": 0,
            keyword: keyword
        }
        if data:   # 若是非空
            returned["total"] = 1
            returned["books"] = cls.__cut_book_data(data)
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned["total"] = data["total"]  # data["books"] 是list，元素是dict
            returned["books"] = [cls.__cut_book_data(book) for book in data["books"]]  # returned["books"] 是[{},{},]

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            "title": data["title"],
            "publisher": data["publisher"],
            "pages": data["pages"] or "",  #
            "author": "、".join(data["author"]),  # list ->str
            "prices": data["prices"],
            "summary": data["summary"] or "",  #
            "image": data["image"],

        }
        return book
