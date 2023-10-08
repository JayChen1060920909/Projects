from flask import Flask, redirect, render_template, request, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' # Things you have to set up before creating a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5) # Deciding the session time

db = SQLAlchemy(app) # creating a database

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def home():
    return render_template("Home.html")

@app.route("/login", methods=["POST",'GET'])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['nm']

        session['user'] = user

        # 先以名字進行查詢
        found_user = users.query.filter_by(name=user).first()

        #如果有的話就把user的email加進去session list裡面, 如果沒有的話就加入一筆新資料到資料庫
        if found_user:
            flash(f"Welcome back {user}!")
            session['email'] = found_user.email
        else:
            flash(f"Hello {user}!, Nice to meet you!!")
            usr = users(user ,"")
            db.session.add(usr)
            db.session.commit()

        return redirect(url_for('user_page'))
    else:
        if "user" in session:
            flash("Already Logged in!")
            return redirect(url_for('user_page'))
        return render_template("login.html")

@app.route('/logout')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f"You have been logged out, {user}!", "info")
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login') )


@app.route('/user', methods=["POST",'GET'])
def user_page():
    email = None
    if 'user' in session:
        user = session['user']

        if request.method == "POST":
            email = request.form['email'] # 使用者輸入的email
            session['email'] = email #也建立一個session
            found_user = users.query.filter_by(name=user).first() # 找到user之後要做的事情
            found_user.email = email # 更新使用者新輸入的email
            db.session.commit() # 每次更新完就要儲存 commit 一次

            flash("Email was saved!!")

        else:
            if "email" in session:
                email = session['email']
            return render_template("user_page.html",content=user, email=email)
    else:
        flash("You are not logged in! ")
        return redirect(url_for('login'))

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)

