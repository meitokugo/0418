
#此文件是来创建数据库的  flask_sqlalchemy数据库框架
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(40), unique=True, nullable=True)

    # db.relationship() 的第一个参数表明这个关系的另一端是哪个模型
    # db.relationship() 中的backref 参数向User 模型中添加一个role 属性
    book = db.relationship('Book', backref='user')

# 类可用来描述相同属性和方法的集合，一对多， 多的关系
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # 设置多表属性
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
