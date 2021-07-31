# python imports

# project imports
from app import db
from .shared.base_mixin import BaseMixin
from .shared.default_values import default_uuid


class TimeModel(BaseMixin, db.Model):

    __tablename__ = 'times'

    # columns
    sk_time = db.Column(db.String, primary_key=True, default=default_uuid)
    time = db.Column(db.Time, unique=True, nullable=False)

    # print function
    def __repr__(self):
        return str(self.time)