# utf-8
from flask import Flask, request
from infraestructure.database import db, migrate
from infraestructure.db_conf import get_conf
from models import Product, User, Role, Permission, Brand, Logo, Category


app = Flask(__name__)
db_conf = get_conf()
FULL_URL_DB = f'postgresql://{db_conf.db.user}:{db_conf.db.password}@{db_conf.db.host}/{db_conf.db.name}'
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'i_like_coffee'


db.init_app(app)
migrate.init_app(app, db)


@app.route('/category', method=['POST'])
def add_category():
    body = request.get_json()
    category = Category()
    return f'Hello'


@app.route('/products')
def get_all_products():
    product = Product.query.all()
    app.logger.debug(f'listado personas:{product}')
    # return render_template('index.html', product=product)
    response = {
        'product': product
    }
    return response, 200

@app.route('/')
def start2():
    return "Hello"

#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

#
# @app.route('/classify/v1', methods=["POST"])
# def classify_text():
#     body = request.get_json()
#
#     response = {
#     }
#     return response, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
