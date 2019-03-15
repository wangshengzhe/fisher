""""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author: 王圣哲
date:   2019/3/14
Description:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# from flask import Flask, current_app, request, Request
#
#
#
# app = Flask(__name__)
# ctx = app.app_context()
# ctx.push()
#
# a = current_app
# d = current_app.config["DEBUG"]
# ctx.pop()



##########################################

# class A:
#     def __enter__(self):
#         a = 1
#     def __exit__(self):
#         b = 2
#
# with A() as obj_A:
#     pass


class Myresource:
    def __enter__(self):
        print("connect to resource")
        return self

    def __exit__(self, a, b, c):
        if c:
            print("process exception")
        else:
            print("no exception")
        print("close resource connection")

    def query(self):
        print("query data")


try:
    with Myresource() as resource:
        1/0
        resource.query()
except Exception as ex:
    pass

