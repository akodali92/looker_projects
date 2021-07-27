# python imports
from flask import flash, redirect, render_template, url_for

# project imports
from app import app
from .forms.person_form import PersonForm
from .models.persons import PersonModel
from app.forms import person_form


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

@app.route("/persons/new", methods=['GET', 'POST'])
def new_person():

    # generate form
    form = PersonForm()

    # for successful submission
    if form.validate_on_submit():

        # display success
        flash(f"{form.first_name.data} {form.last_name.data} created!")
        # redirect
        return redirect(url_for('persons'))
    # else return page
    return render_template('persons_new.html', form=form)
