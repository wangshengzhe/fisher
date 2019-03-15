""""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author: 王圣哲
date:   2019/3/14
Description:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
import threading
import time


def worker():
    print("i am thread")
    t = threading.current_thread()
    print(t.getName())


new_t = threading.Thread(target=worker, name="wang_thread")
new_t.start()


t = threading.current_thread()

time.sleep(3)
print("hello threading")
print(t.getName())
