
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.model import User, Book


##结构-+-manage.py
 #|
 #+-app-+-__init__.py
 #  　  |
 #    　+-models.py
 #这样才能from app import models.py,
 #或者 from app.models import db
app = create_app()             # 初始化app,为实例提供各种配置
manager = Manager(app)   # flask_script
migrate = Migrate(app,db)   # 用于迁移数据库

#创建一个正确的请求上下文最简单的方法就是使用 test_request_context 方法
##注册程序，数据库，实例模型，使其能直接导入交互式的shell上下文（代码上下文：python中可切换上下文以便显示或隐藏窗口面板）
def make_shell_context():
    return dict(app=app, db=db, User=User)

# 当导入的时候可以直接使用app db, user
#python shell 窗口可以输入编辑，召回语句，直到按下return，则会编译和执行

#数据库迁移的目的是使得命令行窗口接口或者Flask-script能够对数据库进行操作
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    # 启动的时候需要在控制台中 输入 python xx.py runserver -h地址  -p端口
    manager.run()