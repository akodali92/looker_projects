# python imports
from sqlalchemy.orm import column_property

# project imports
from app import db
from .shared.base_mixin import BaseMixin
from .shared.default_values import default_uuid

class ProjectModel(BaseMixin, db.Model):

    __tablename__ = 'projects'
    __table_args__ = (db.UniqueConstraint('project', 'client', 'service_line', 'practice', name='unique_project_record'),)

    # columns
    sk_project = db.Column(db.String, primary_key=True, default=default_uuid)
    project = db.Column(db.String, nullable=False)
    client = db.Column(db.String, nullable=False)
    is_billable = db.Column(db.Boolean, default=False)
    service_line = db.Column(db.String, nullable=False)
    practice = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)

    project_record = column_property(project + " - " + client + ' (' + service_line + ': ' + practice + ')')


    # print function
    def __repr__(self):
        return self.project_record