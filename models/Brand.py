from datetime import datetime
from app import db


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logo_id = db.Column(db.Integer, db.ForeignKey('logo.id'), nullable=True)
    brand_name = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    delete_date = db.Column(db.DateTime())
