#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

# test 是链接的数据库
app.config['MONGODB_SETTINGS'] = {'db': 'test'}

# 实例化
db = MongoEngine(app)

@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    app.run()