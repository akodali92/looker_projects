# python imports
from flask import render_template

# project imports
from app import app


# setup routes
@app.route("/")
def home():
    return render_template('home.html')