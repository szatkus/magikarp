from flask_sqlalchemy import SQLAlchemy

from application import application

db = SQLAlchemy(application)

class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80))
