# python imports
from sqlalchemy.orm import column_property

# project imports
from app import db
from .default_values import default_uuid

class PersonModel(db.Model):

    __tablename__ = 'persons'

    # columns
    sk_person = db.Column(db.String, primary_key=True, default=default_uuid)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    company = db.Column(db.String)
    role = db.Column(db.String)

    full_name = column_property(first_name + " " + last_name)
    person_record = column_property(first_name + " " + last_name + " - " + company + ", " + role)


    # print function
    def __repr__(self):
        return self.person_record

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()