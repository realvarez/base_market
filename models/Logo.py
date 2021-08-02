from datetime import datetime
from app import db


class Logo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.relationship('Brand', backref='logo', lazy=True)
    path = db.Column(db.String(600), nullable=False)
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    delete_date = db.Column(db.DateTime())
