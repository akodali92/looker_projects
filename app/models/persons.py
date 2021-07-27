# python imports
from sqlalchemy.orm import column_property

# project imports
from app import db
from .shared.base_mixin import BaseMixin
from .shared.default_values import default_uuid

class PersonModel(BaseMixin, db.Model):

    __tablename__ = 'persons'
    __table_args__ = (db.UniqueConstraint('first_name', 'last_name', 'company', 'role', 'email_address', name='unique_person_record'),)

    # columns
    sk_person = db.Column(db.String, primary_key=True, default=default_uuid)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False)

    full_name = column_property(first_name + " " + last_name)
    person_record = column_property(first_name + " " + last_name + " - " + company + ", " + role)

    


    # print function
    def __repr__(self):
        return self.person_record