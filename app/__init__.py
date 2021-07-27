# python imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# project imports


# initialize app
app = Flask(__name__)

# config app
# app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = '123456'
# create db instance
db = SQLAlchemy(app)

# import routes
from app import routes