from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import  get_postgresql_db_credential


def create_app(debug=False):
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] =get_postgresql_db_credential(database="technicaltest",user_name="technicaltestuser",password='1234',host="localhost")
    return app
app_instance = create_app()
db = SQLAlchemy(app_instance)

