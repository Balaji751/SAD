import os
import datetime
from flask import Flask,session,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
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
    return render_template("index.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method =="POST":

        email=request.form.get("email")
        password=request.form.get("psw")
        dt=datetime.datetime.now()
        data=Registers(email=email,password=password,timestamp=dt)
        db.session.add(data)
        db.session.commit()
        if not email:
            text="Please enter email to register"
            return render_template("registernames.html",name=text,msg="ERROR")
        elif not password:
            text="Please provide password"
            return render_template("registernames.html",name=text,msg="ERROR")
        else:
            return render_template("registernames.html",msg="SUCCESS")
    return render_template("index.html")

@app.route("/admin")
def admin():
    data1 = Registers.query.all()
    return render_template("registerlist.html", name=data1)


def main():
    app.app_context().push()
    db.create_all()



if __name__ == "__main__":
    # with app.app_context():
    main()