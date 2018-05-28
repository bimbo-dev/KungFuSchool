from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, DateField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    id = HiddenField('Id')
    last_name = StringField('Last Name', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    other_names = StringField('Other Names')
    phone_number = StringField('Phone Number')
    email_address = StringField('Email Address')
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    address = StringField('Address')


class StudentBindingModel(object):
    id = None
    last_name = None
    first_name = None
    other_names = None
    phone_number = None
    email_address = None
    date_of_birth = None
    address = None