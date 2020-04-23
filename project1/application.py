import os
import datetime
from flask import Flask,session,render_template,request,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy import or_
from models import *


app=Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)

@app.route("/")

def index():

    return render_template("index.html",flag=True)

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method =="POST":

        email=request.form.get("email")
        password=request.form.get("psw")
        dt=datetime.datetime.now()
        data2 = Registers.query.all()
        for user in data2:
            if email == user.email:
                return "<h2 Style='color: red;text-align:center'>You already have registered !Please Login </h2>"
        if not email:
            text = "Please enter username to register"
            return render_template("registernames.html", name=text, msg="ERROR")
        elif not password:
            text="Please provide password"
            return render_template("registernames.html", name=text ,msg="ERROR")
        else:
            data = Registers(email=email,password=password,timestamp=dt)
            db.session.add(data)
            db.session.commit()
            return render_template("registernames.html",msg="SUCCESS")
    return render_template("index.html", flag=True)

@app.route("/admin")
def admin():
    data1 = Registers.query.all()
    return render_template("registerlist.html", name=data1)


@app.route("/auth",methods=["GET","POST"])
def userhome():
    if(request.method=="POST"):
        email=request.form.get("email")
        password=request.form.get("psw")
        if not email:
            text = "Please enter email to register"
            return render_template("registernames.html", name=text, msg="ERROR")
        elif not password:
            text="Please provide password"
            return render_template("registernames.html", name=text ,msg="ERROR")
        data3=Registers.query.all()
        for each in data3:
            if each.email==email:
                if each.password==password:
                    session["email"]=each.email
                    return redirect("/user")
        return render_template("index.html",flag=False)
    if(request.method=="GET"):
        return redirect(url_for('register'))

@app.route("/logout")
def sessiontimeout():
    session.pop("email",None)
    return redirect(url_for('register'))

@app.route("/user",methods=["GET","POST"])
def user():
    if session.get("email") is None:
         return redirect(url_for('register'))
    if (request.method == "POST"):
        search = request.form.get("search")
        print(search)
        search_query="%"+search+"%"
        
        books = Book.query.filter(or_(Book.title.like(search_query), Book.author.like(search_query), Book.isbn.like(search_query))).all()
        print(books)
        c=0
        for each in books:
            c=c+1
        print(c)
        if books == []:
            return render_template("user.html",name=books, flag=False,var=True)
        return render_template("user.html",name=books,flag=False)
    return render_template("user.html",flag=True)

@app.route("/book",methods=["GET"])
@app.route("/book/<isbn>")
def book(isbn):
    return render_template("book.html",isbn=isbn)

def main():
    app.app_context().push()
    db.create_all()



if __name__ == "__main__":
    # with app.app_context():
    main()