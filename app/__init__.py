
import os

from flask import Flask, url_for
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

#创建和设置app
#create_app是个应用工厂函数
def create_app():
    #创建flask实例__name__为当前模块名称
    app = Flask(__name__)

    # -----------  这里可以单独写到配置文件中 为应用设置配置
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'alflxjklwelropnona'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(os.path.join(basedir, 'data.sqlite'))
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    #  ------------  配置文件 结束
    # 初始化数据库
    db.init_app(app)

    # 图书管理系统
    from app.view import book

    # 统一对外接口蓝本
    app.register_blueprint(book)

    return app

# 测试
# app = create_app()
# with app.test_request_context():
# print(url_for('index'))

