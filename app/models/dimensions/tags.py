# python imports

# project imports
from app import db
from ..shared.base_mixin import BaseMixin

class TagDimension(BaseMixin, db.Model):

    __tablename__ = 'tag_dimension'

    # columns
    sk_tag = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String, nullable=False)

    # print function
    def __repr__(self):
        return self.tag