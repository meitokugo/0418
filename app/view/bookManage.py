#视图函数，视图是一个应用请求进行响应的函数，视图返回数据，flask把数据变成出去的响应
from app import db
from app.view import book
from app.model import User, Book
from flask import render_template, flash, request, redirect, url_for

#关联url中的视图函数
@book.route('/', methods=["GET", "POST"])
# 主页展示， 添加
def index():
    #如果用户提交表单，将会是‘post'，这种情况下开始验证用户的输入内容
    if request.method == "POST":
        #request.form是一个特殊的dict字典，映射提交表单的键和值，用户将输入两个值
        author = request.form['author']
        book = request.form['book']
        # all([])只有当列表里的元素都有值（不为none/0/空字符串）的时候，才会返回true
        if not all([author, book]):
            flash('不能为空')
             #redirect重定位函数，指定url 
            return redirect(url_for('book.index'))
            #query .fiter_by为sqlite3查询语句
        getAuther = User.query.filter_by(name=author).first()

        #验证是否成功
        if getAuther:  # 判断如果存在
            user = Book(name=book, user=getAuther)
            # db.session.add(add_book)
            # db.session.commit()
        #若不存在这插入新数据到数据库
        else:         # 如果不存在
            user = User(name=author)
            book = Book(name=book)
            user.book = [book]
         #添加到 session  
        db.session.add(user)
        #添加提交数据操作，session.close关闭session
        db.session.commit()
        flash('添加成功')
        #redirect重定位函数，指定url
        return redirect(url_for('book.index'))
    else:
        #循环遍历出来的结果打印出来,query，为sqlite3查询语句
        queryObj = User.query.all()
        return render_template('book/index.html', queryObj=queryObj)


# 删除书本
@book.route('/deleteBook/<int:delid>')
def delete(delid):
    if Book.query.get(delid) is not None:
        # 直接删除并提交
        db.session.delete(Book.query.get(delid))
        db.session.commit()
    return redirect(url_for('book.index'))


# 删除作者
@book.route('/delauth/<int:delid>')
def delauth(delid):
    if User.query.get(delid) is not None:
        # 获取用户名称
        getuser = User.query.filter_by(id=delid).first()
        # 循环书本
        for user in getuser.book:
            # Book.query.filter_by(id=delid).first()   = Book.query.get(user.id)
            # db.session.delete(Book.query.get(user.id))
            db.session.delete(Book.query.filter_by(id=delid).first())
             #直接删除并提交
        db.session.delete(getuser)
        db.session.commit()
        return redirect(url_for('book.index'))
    return redirect(url_for('book.index'))
