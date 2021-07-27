# python imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

from sqlalchemy.orm import column_property

# project imports


# initialize app
app = Flask(__name__)

# config app
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# create db instance
db = SQLAlchemy(app)

class Person(db.Model):

    __tablename__ = 'persons'

    # columns
    sk_person = db.Column(db.String, primary_key=True, default=str(uuid4()).replace('-',''))
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    full_name = column_property(first_name + " " + last_name)
    company = db.Column(db.String)
    role = db.Column(db.String)

    # print function
    def __repr__(self):
        return f"{self.full_name} - {self.company}, {self.role}"

# setup routes
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

# run app
if __name__ == '__main__':
    app.run()
