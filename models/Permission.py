from app import db
from datetime import datetime

role_permissions = db.Table('role_permissions',
                            db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
                            db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True),
                            db.Column('status', db.Boolean, default=True))


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    delete_date = db.Column(db.DateTime())

