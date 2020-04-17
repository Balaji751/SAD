from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method =="POST":

        email=request.form.get("email")
        print(email)
        password=request.form.get("psw")
        print(password)
        return render_template("register.html",email=email)
    return render_template("index.html")