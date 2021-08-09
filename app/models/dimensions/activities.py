# python imports
from sqlalchemy.orm import column_property

# project imports
from app import db
from ..shared.base_mixin import BaseMixin


class ActivityDimension(BaseMixin, db.Model):

    __tablename__ = 'activity_dimension'
    __table_args__ = (db.UniqueConstraint('activity', 'project', name='unique_activity_record'),)


    # columns
    sk_activity = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String, unique=True, nullable=False)
    is_activity_billable = db.Column(db.Boolean, nullable=False)
    project = db.Column(db.String, nullable=False)
    is_project_billable = db.Column(db.Boolean, nullable=False)
    project_client = db.Column(db.String, nullable=False)
    project_service_line = db.Column(db.String, nullable=False)
    project_practice = db.Column(db.String, nullable=False)
    project_type = db.Column(db.String, nullable=False)

    activity_record = column_property(activity + " (" + project + ")")


    # print function
    def __repr__(self):
        return self.activity_record