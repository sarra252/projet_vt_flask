from . import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.Text, nullable=True)
    url = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(100), nullable=True)
