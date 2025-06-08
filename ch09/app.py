from flask import Flask, request, render_template, session, redirect, url_for
from functools import wraps
from auth.forms import LoginForm, EditForm
from routings.demo_a.urls import demo_a
from routings.demo_b.urls import demo_b
import pymysql

from settings.config import Mysql_Config

app = Flask(__name__)
app.secret_key="sadfafklweoaidvwenfkloijo@*ii*lncoheofnl"
app.register_blueprint(demo_b)

def login_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view_func(*args, **kwargs)
    return wrapper

def check_user(username, password):
    connections = pymysql.connect(**Mysql_Config)
    try:
        with connections.cursor() as cursor:
            sql = "select * from users where username = %s and password = %s"
            cursor.execute(sql,(username,password))
            result = cursor.fetchone()
            return result is not None
    finally:
        connections.close()



# 指到 index 頁面
@app.route("/", methods=["GET","POST"])
@login_required
def index():
    return render_template("index.html")

@app.route("/about")
@login_required
def about():
    return render_template("about.html")

@app.route("/users")
@login_required
def user_list():
    connections = pymysql.connect(**Mysql_Config)
    try:
        with connections.cursor() as cursor:
            sql = "select * from users"
            cursor.execute(sql)
            users = cursor.fetchall()
    finally:
        connections.close()

    return render_template("users.html", users=users )

@app.route("/users/<int:user_id>/edit", methods=['GET','POST'])
@login_required
def edit_user(user_id):
    form = EditForm()
    error = None

    if form.validate_on_submit():
        new_password = form.password.data
        connections = pymysql.connect(**Mysql_Config)
        try:
            with connections.cursor() as cursor:
                sql = "update users set password = %s where id = %s"
                cursor.execute(sql, (new_password, user_id))
                connections.commit()
            return redirect(url_for('user_list'))
        finally:
            connections.close()

    return render_template("edit_user.html", form=form, user_id=user_id)


@app.route('/login', methods=['GET','POST'])
def login():
    # if session.get('logged_in'):
    #     return redirect(url_for('index'))
    #
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        # if form.username.data == USERNAME and form.password.data == PASSWORD:
        if check_user(form.username.data, form.password.data):
            session['logged_in'] = True
            session['username'] = form.username.data
            return redirect(url_for('index'))
        else:
            error = '帳密或密碼錯誤'
    return render_template('login.html', form=form, error= error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', use_reloader=True)
