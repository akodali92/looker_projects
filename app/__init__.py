# python imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# project imports


# initialize app
app = Flask(__name__)

# config app
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# create db instance
db = SQLAlchemy(app)

# import routes
from app.routes import index, persons, projects, events

# import models
from app.models import persons, projects, events, dates, times