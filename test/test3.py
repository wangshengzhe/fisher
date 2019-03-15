""""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author: 王圣哲
date:   2019/3/14
Description:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
import threading
import time
from werkzeug.local import Local


# class A:
#     b = 1
#
#
# my_obj = A()
#
#
# def worker():
#     print(my_obj.b)
#     my_obj.b = 2
#
#
# new_t = threading.Thread(target=worker, name="wang_thread")
# new_t.start()
#
# time.sleep(1)
#
# print(my_obj.b)  # 多线程资源共享

##############################################################


class A:
    b = 1


my_obj = Local()
my_obj.b = 1


def worker():
    #print("in new thread b is ====", my_obj.b)
    my_obj.b = 2
    print("in new thread b is ", my_obj.b)


new_t = threading.Thread(target=worker, name="wang_thread")
new_t.start()

time.sleep(1)

print("in main thread b is ", my_obj.b)  # 多线程