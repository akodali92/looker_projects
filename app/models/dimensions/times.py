# python imports

# project imports
from app import db
from ..shared.base_mixin import BaseMixin


class TimeDimension(BaseMixin, db.Model):

    __tablename__ = 'time_dimension'

    # columns
    sk_time = db.Column(db.String, primary_key=True)
    time = db.Column(db.Time, unique=True, nullable=False)

    # print function
    def __repr__(self):
        return str(self.time)