#初始化蓝图
from flask import Blueprint
#蓝图是组织一组相关视图及其代码的方式，蓝图方式是把它们注册到蓝图，然后在工厂函数中 把蓝图注册到应用。
# 生成蓝图
book = Blueprint('book', __name__)
#第一个参数为名称，第二个为让蓝图知道在哪儿定义，第三个为添加到所有与蓝图关联的url上
# 导入执行视图
from . import bookManage