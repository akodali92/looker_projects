# python imports
from sqlalchemy.orm import column_property
from uuid import uuid4

# project imports
from app import db

class PersonModel(db.Model):

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