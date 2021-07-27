# python imports
from flask import Blueprint, render_template

# project imports
from app import app
from ..models.persons import PersonModel



@app.route("/persons")
def persons():
    persons = PersonModel.query.all()
    return render_template('persons.html', persons=persons)