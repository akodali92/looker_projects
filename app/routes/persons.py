# python imports
from flask import Blueprint, flash, redirect, render_template, url_for

# project imports
from app import app
# from ..forms.person_form import PersonForm
from ..models.persons import PersonModel

home_bp = Blueprint('home_bp', __name__)
about_bp = Blueprint('about_bp', __name__)



@app.route("/persons")
def persons():
    persons = PersonModel.query.all()
    return render_template('persons.html', persons=persons)

# @app.route("/persons/new", methods=['GET', 'POST'])
# def new_person():

    # # generate form
    # form = PersonForm()
    

    # # for successful submission
    # if form.validate_on_submit():
    #     first_name = form.first_name.data
    #     last_name = form.last_name.data
    #     company = form.company.data
    #     role=form.company.data
    #     person = PersonModel(first_name=first_name, last_name=last_name, company=company, role=role)
    #     try:
    #         person.save_to_db()
    #         # display success
    #         person_form_data = f"{form.first_name.data} {form.last_name.data}"
    #         flash(f"{person_form_data} created!", "success")
    #         # redirect
    #         return redirect(url_for('persons'))
    #     # else return page
    #     except:
    #         flash("Unsuccessful, please check data", "danger")
    # return render_template('persons_new.html', form=form)
