# -*- coding: utf-8 -*-


###############################################################################################
from app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=81)

############################################################################################

# app = Flask(__name__)
# app.config.from_object("config")
#
# from app.web import book
#
# if __name__ =="__main__":
#     app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=81)

# app = Flask(__name__)
# print("id为", id(app), "的app实例化")
# app.config.from_object("config")  # 模块路径   读取配置文件
# print(app.config["DEBUG"])
#
#
# from app.web import book

