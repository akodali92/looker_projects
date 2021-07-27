# python imports

# project imports
from app import db


class BaseMixin(db.Model):
    '''Base model that all models inherit'''

    __abstract__ = True

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
