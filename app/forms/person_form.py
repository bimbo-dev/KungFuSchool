from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired


class PersonForm(FlaskForm):
    id = HiddenField('Id')
    last_name = StringField('Last Name', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    other_names = StringField('Other Names')
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    email_address = StringField('Email Address', validators=[DataRequired()])
