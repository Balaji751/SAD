from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class Users(db.model()):
    __tablename__= "users"
    email=db.Column(db.String,nullable=False)
    password=db.Column(db.password,nullable=False)
    timestamp=db.Column(db.String,nullable=False)

db.session.add(Users(email=email,password=password,timestamp=timestamp))