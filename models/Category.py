from datetime import datetime
from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(250), nullable=False)
    category_description = db.Column(db.String(250))
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    delete_date = db.Column(db.DateTime())

    def __str__(self):
        return (
            f'Id:{self.id}, '
            f'first_name:{self.category_name}, '
            f'last_name:{self.category_description}, '
        )
