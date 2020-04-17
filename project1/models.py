from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Registers(db.Model):
    __tablename__= "Registers"
    email=db.Column(db.String,primary_key=True,nullable=False)
    password=db.Column(db.String,nullable=False)
    timestamp=db.Column(db.String,nullable=False)