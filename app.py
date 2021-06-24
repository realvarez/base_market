# utf-8
from flask import Flask, render_template
from infraestructure.database import db, migrate
from infraestructure.db_conf import get_conf
from models import Product, User, Role, Permission


app = Flask(__name__)
db_conf = get_conf()
FULL_URL_DB = f'postgresql://{db_conf.db.user}:{db_conf.db.password}@{db_conf.db.host}/{db_conf.db.name}'
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate.init_app(app, db)


@app.route('/index')
@app.route('/index.html')
def start():
    product = Product.query.all()
    count = Product.query.count()
    app.logger.debug(f'listado personas:{product}')
    app.logger.debug(f'cuenta personas:{count}')
    return render_template('index.html',
                           product=product,
                           product_count=count)


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
