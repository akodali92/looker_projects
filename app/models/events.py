# python imports

# project imports
from app import db
from .shared.base_mixin import BaseMixin
from .shared.default_values import default_uuid


class EventModel(BaseMixin, db.Model):

    __tablename__ = 'events'

    # columns
    sk_event = db.Column(db.String, primary_key=True, default=default_uuid)
    event_name = db.Column(db.String, unique=True, nullable=False)

    # print function
    def __repr__(self):
        return self.event_name