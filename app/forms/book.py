""""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author: 王圣哲
date:   2019/3/14
Description:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message="you are error")])  # message 自定义错误信息,DataRequired()防止空格通过验证
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


