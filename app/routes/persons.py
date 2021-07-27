# python imports
from flask import redirect, render_template, request, url_for

# project imports
from app import app
from ..models.persons import PersonModel



@app.route("/persons")
def persons():
    persons = PersonModel.query.all()
    return render_template('persons.html', persons=persons)


@app.route("/persons/new", methods=['POST'])
def persons_new():
    form_dict = dict(request.form)
    person_record = PersonModel(**form_dict)
    try:
        person_record.save_to_db()
        print(f"Inserted: {person_record.sk_person}")
    except Exception as e:
        print(f"Not inserted: {e}")
    return redirect(url_for('persons'))
