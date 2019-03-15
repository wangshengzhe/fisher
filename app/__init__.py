""""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author: 王圣哲
date:   2019/3/13
Description:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.secure")  # 模块路径
    app.config.from_object("app.setting")
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web   #
    app.register_blueprint(web)   # 将 蓝图对象注册在app上
    # return app
