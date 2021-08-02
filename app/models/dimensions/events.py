# python imports

# project imports
from app import db
from ..shared.base_mixin import BaseMixin
from ..shared.default_values import default_uuid


class EventDimension(BaseMixin, db.Model):

    __tablename__ = 'event_dimension'

    # columns
    sk_event = db.Column(db.String, primary_key=True, default=default_uuid)
    event = db.Column(db.String, unique=True, nullable=False)
    event_type = db.Column(db.String)

    # print function
    def __repr__(self):
        return self.event