# python imports
from flask import redirect, render_template, url_for

# project imports
from app import app
from .models.persons import PersonModel


# setup routes
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/persons")
def persons():

    persons = PersonModel.query.all()
    return render_template('persons.html', persons=persons)

@app.route("/persons/new")
def new_person():
    person = PersonModel(first_name='Aneesh', last_name='Kodali', company='Analytics8', role='Consultant')
    person.save_to_db()
    return redirect(url_for('persons'))