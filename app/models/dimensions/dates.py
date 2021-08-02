# python imports

# project imports
from app import db
from ..shared.base_mixin import BaseMixin


class DateDimension(BaseMixin, db.Model):

    __tablename__ = 'date_dimension'

    # columns
    sk_date = db.Column(db.String, primary_key=True)
    date = db.Column(db.Date, unique=True, nullable=False)

    # print function
    def __repr__(self):
        return str(self.date)