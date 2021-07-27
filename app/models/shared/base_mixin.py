# python imports

# project imports
from app import db


class BaseMixin(db.Model):
    '''Base model that all models inherit'''

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
