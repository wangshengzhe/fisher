""""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author: 王圣哲
date:   2019/3/13
Description:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
from flask import Blueprint


web = Blueprint("web", __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
from app.web import user