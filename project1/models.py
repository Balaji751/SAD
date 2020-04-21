from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Registers(db.Model):
    __tablename__= "Registers"
    email=db.Column(db.String,primary_key=True,nullable=False)
    password=db.Column(db.String,nullable=False)
    timestamp=db.Column(db.String,nullable=False)

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    pub_year = db.Column(db.Integer, nullable=False)
    revs = db.Column(db.String, nullable=True)