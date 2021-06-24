from datetime import datetime
from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    product_name = db.Column(db.String(250), nullable=False)
    product_code = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String(250))
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    delete_date = db.Column(db.DateTime())

    def __str__(self):
        return (
            f'Id:{self.id}, '
            f'first_name:{self.product_name}, '
            f'last_name:{self.product_description}, '
        )
