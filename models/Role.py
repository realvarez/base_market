from app import db
from datetime import datetime


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User', backref='role', lazy=True)
    name = db.Column(db.String(250), nullable=False)
    status = db.Column(db.Boolean(), nullable=False, default=True)
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    delete_date = db.Column(db.DateTime(), nullable=True, default=None)

