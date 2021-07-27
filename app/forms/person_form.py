# python imports
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# project imports


class PersonForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    submit = SubmitField("Add Person")