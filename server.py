from flask import Flask,request

from controllers.dishes import DishesByCategory
from controllers.categories import CategoryAll
from flask_restful import Api
from config import DBUSER,DBHOST,DBPASS
from flask_cors import CORS
from db import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
app.config['SECRET_KEY'] = 'yt56h56h5h456h456y4yu46u576i'
CORS(app)
db.init_app(app)
api = Api(app)


with app.app_context():
    db.create_all()

api.add_resource(DishesByCategory,'/dishes')
api.add_resource(CategoryAll,'/categories')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
