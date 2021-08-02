from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_role = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    user_name = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean(), default=True)
    products = db.relationship('Products', backref='user', lazy=True)
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    delete_date = db.Column(db.DateTime(), nullable=True, default=None)
