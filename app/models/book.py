""""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author: 王圣哲
date:   2019/3/14
Description:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)  # 数字，主键，自增长  主键默认不会重复
    title = Column(String(50), nullable=False)  # 字符串最长50，不能为空
    author = Column(String(30), default="佚名")
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)  # 不能重复
    summary = Column(String(1000))
    image = Column(String(50))   # 图片

    def sample(self):
        pass

